from importlib import import_module
from pathlib import Path
import shutil

PipelineDados = import_module("src.data.01_pipeline_dados").PipelineDados
DatasetAnalitico = import_module("src.data.02_dataset_analitico").DatasetAnalitico


def test_pipeline_creates_processed_dir(tmp_path):
    pipeline = PipelineDados(tmp_path)
    pipeline.ensure_directories()
    assert (tmp_path / "data/processed").exists()


def test_pipeline_processes_csv_files(tmp_path):
    (tmp_path / "example.csv").write_text("id,value\n1,2\n", encoding="utf-8")
    pipeline = PipelineDados(tmp_path)
    dfs = pipeline.run()
    assert isinstance(dfs, dict)
    assert "example" in dfs
    assert (tmp_path / "data/processed/example_processado.csv").exists()


def test_dataset_analitico_is_built(tmp_path):
    source_dir = Path(__file__).resolve().parents[1] / "data/raw"
    raw_dir = tmp_path / "data/raw"
    raw_dir.mkdir(parents=True)
    required_sources = [
        "Produtos.csv",
        "Vendas_24m.csv",
        "Forecast_Comercial.csv",
        "Estoque_Atual.csv",
        "Historico_Estoque.csv",
        "Carteira_Pedidos.csv",
        "Ordens_Producao.csv",
        "Lead_Times.csv",
    ]
    for filename in required_sources:
        shutil.copy2(source_dir / filename, raw_dir / filename)

    dataset = DatasetAnalitico(tmp_path)
    df = dataset.build()
    assert not df.empty
    assert "sku" in df.columns
    assert "mes" in df.columns
    assert "risco_ruptura_hipotese" in df.columns
