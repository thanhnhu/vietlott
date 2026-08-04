import pandas as pd
import pytest

from vietlott.datasource import load_data, load_product


def test_load_product_jsonl():
    df = load_product("power_655")
    assert {"date", "id", "result"}.issubset(df.columns)
    assert isinstance(df.iloc[0]["result"], list)
    assert all(isinstance(n, int) for n in df.iloc[0]["result"])


def test_load_excel_from_number_columns(tmp_path):
    pytest.importorskip("openpyxl")
    path = tmp_path / "draws.xlsx"
    pd.DataFrame(
        {
            "date": ["2021-01-01", "2021-01-03"],
            "id": ["00001", "00002"],
            "num_1": [1, 10],
            "num_2": [2, 20],
            "num_3": [3, 30],
            "num_4": [4, 40],
            "num_5": [5, 50],
            "num_6": [6, 55],
        }
    ).to_excel(path, index=False)

    df = load_data(path)
    assert list(df.columns) == ["date", "id", "result"]
    assert df.iloc[0]["result"] == [1, 2, 3, 4, 5, 6]
    assert df.iloc[1]["result"] == [10, 20, 30, 40, 50, 55]


def test_load_excel_with_result_column(tmp_path):
    pytest.importorskip("openpyxl")
    path = tmp_path / "draws.xlsx"
    pd.DataFrame({"id": ["00001"], "result": ["[7, 8, 9]"]}).to_excel(path, index=False)

    df = load_data(path)
    assert df.iloc[0]["result"] == [7, 8, 9]


def test_unsupported_extension(tmp_path):
    path = tmp_path / "draws.parquet"
    path.write_bytes(b"")
    with pytest.raises(ValueError, match="unsupported data source"):
        load_data(path)
