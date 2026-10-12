from pathlib import Path
import shutil

import pandas as pd
import pytest

from src.models.forecast_demanda import PrevisaoDemanda, metricas_previsao


def small_fixture():
    months = pd.date_range("2024-01-01", periods=18, freq="MS")
    rows = []
    for month in months:
        seasonal = 2 if month.month == 1 else 1
        for sku, family, base in [("SKU-A", "Escolar", 100), ("SKU-B", "Escolar", 50)]:
            for channel, share in [("Direto", 0.6), ("KA-01", 0.4)]:
                rows.append(
                    {
                        "mes": month,
                        "sku": sku,
                        "canal": channel,
                        "quantidade": base * seasonal * share,
                    }
                )
    return pd.DataFrame(rows), pd.DataFrame(
        [{"sku": "SKU-A", "familia": "Escolar"}, {"sku": "SKU-B", "familia": "Escolar"}]
    )


def test_forecast_reconciles_channels_and_marks_output_as_forecast():
    sales, products = small_fixture()
    output = PrevisaoDemanda().predict(sales, products, ["2025-07", "2025-08"])

    assert output["status_previsao"].eq("OK").all()
    assert output["natureza_dado"].eq("previsto").all()
    assert output.groupby(["sku", "mes"])["participacao_canal"].sum().eq(1).all()
    assert output.groupby(["sku", "mes"])["previsao_unidades"].sum().notna().all()


def test_forecast_does_not_use_observations_after_forecast_start():
    sales, products = small_fixture()
    base = PrevisaoDemanda().predict(sales, products, ["2025-07"])
    future_rows = sales[sales["mes"] >= "2025-07"].copy()
    future_rows["quantidade"] *= 1000
    with_future = PrevisaoDemanda().predict(
        pd.concat([sales, future_rows], ignore_index=True), products, ["2025-07"]
    )

    pd.testing.assert_series_equal(
        base["previsao_unidades"], with_future["previsao_unidades"], check_names=False
    )


def test_forecast_reports_insufficient_history_without_fabricating_quantity():
    sales, products = small_fixture()
    short = sales[sales["mes"] >= "2025-01"]
    result = PrevisaoDemanda().predict(short, products, ["2025-07"])

    assert result["status_previsao"].eq("INSUFICIENTE").all()
    assert result["previsao_unidades"].isna().all()
    assert result["motivo_insuficiencia"].notna().all()


def test_forecast_blocks_incomplete_recent_channel_mix():
    sales, products = small_fixture()
    recent_start = sales["mes"].max() - pd.DateOffset(months=2)
    sparse = sales[
        ~((sales["mes"] >= recent_start) & (sales["canal"] == "KA-01"))
    ]

    result = PrevisaoDemanda().predict(sparse, products, ["2025-07"])

    assert result["status_previsao"].eq("INSUFICIENTE").all()
    assert result["previsao_unidades"].isna().all()


def test_metric_definitions_exclude_zero_actuals_only_from_mape():
    metrics = metricas_previsao([10, 0, 20], [12, 8, 18])

    assert metrics["n_pares"] == 3
    assert metrics["n_realizados_zero"] == 1
    assert metrics["wape"] == pytest.approx(12 / 30)
    assert metrics["mape"] == pytest.approx(0.15)
    assert metrics["bias"] == pytest.approx(8 / 30)


def test_rolling_origin_backtest_keeps_method_and_horizon_dimensions():
    sales, products = small_fixture()
    result = PrevisaoDemanda().rolling_origin_backtest(sales, products)

    assert {"origem", "horizonte_meses", "metodo", "realizado"}.issubset(result.columns)
    assert set(result["metodo"].dropna()) == {
        "sazonal_familia_nivel_sku",
        "sazonal_ingenuo",
        "media_movel_3m",
        "ingenuo",
    }
    assert set(result["horizonte_meses"].dropna().unique()) <= {1, 2, 3}


def test_build_generates_october_through_december_from_august_actuals(tmp_path):
    source_dir = Path(__file__).resolve().parents[1] / "data/raw"
    raw_dir = tmp_path / "data/raw"
    raw_dir.mkdir(parents=True)
    for filename in ["Vendas_24m.csv", "Produtos.csv"]:
        shutil.copy2(source_dir / filename, raw_dir / filename)

    forecast = PrevisaoDemanda(tmp_path)
    result = forecast.build()

    assert result["mes"].min() == pd.Timestamp("2026-10-01")
    assert result["mes"].max() == pd.Timestamp("2026-12-01")
    assert len(result) == 50 * 8 * 3
    assert result["status_previsao"].eq("OK").all()
    assert forecast.forecast_path.exists()


def test_commercial_comparison_is_forecast_against_forecast_without_actuals(tmp_path):
    raw_dir = tmp_path / "data/raw"
    raw_dir.mkdir(parents=True)
    pd.DataFrame(
        [
            ["Forecast comercial"],
            [""],
            ["SKU", "Mês", "Previsão unidades"],
            ["SKU-A", "out/25", 120],
            ["SKU-A", "out/25", 30],
        ]
    ).to_csv(raw_dir / "Forecast_Comercial.csv", index=False, header=False)
    forecast = PrevisaoDemanda(tmp_path)
    model_forecast = pd.DataFrame(
        [
            {
                "sku": "SKU-A",
                "mes": pd.Timestamp("2025-10-01"),
                "previsao_unidades": 140,
            },
            {
                "sku": "SKU-A",
                "mes": pd.Timestamp("2025-10-01"),
                "previsao_unidades": 40,
            },
        ]
    )

    comparison = forecast.compare_commercial_forecast(model_forecast)

    assert len(comparison) == 1
    assert comparison.loc[0, "previsao_comercial_unidades"] == 150
    assert comparison.loc[0, "previsao_modelo_unidades"] == 180
    assert comparison.loc[0, "diferenca_unidades"] == 30
    assert comparison.loc[0, "natureza_dado"] == "previsto_vs_previsto"
    assert not comparison.loc[0, "realizado_disponivel"]
