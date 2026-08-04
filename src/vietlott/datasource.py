"""load lottery draw data from multiple sources (jsonl, excel) into a common schema.

common schema columns:
    - ``date``: ISO date string (or date)
    - ``id``: draw id
    - ``result``: ``list[int]`` of drawn numbers

extra columns (``page``, ``process_time``, ...) are preserved when present.
this is the single entry point so strategies do not care whether data comes from
jsonl, excel, or a future source - add a loader here and every consumer benefits.
"""

import json
from pathlib import Path

import pandas as pd

RESULT_COL = "result"
_META_COLS = {"date", "id", "page", "process_time"}


def _coerce_result(value):
    if isinstance(value, str):
        value = json.loads(value)
    return [int(v) for v in value]


def load_jsonl(path, **_ignored) -> pd.DataFrame:
    return pd.read_json(path, lines=True, dtype=object, convert_dates=False)


def load_excel(path, number_columns=None, **_ignored) -> pd.DataFrame:
    """load an excel workbook.

    if there is no ``result`` column, the drawn numbers are assembled from
    ``number_columns`` (defaults to every column that is not draw metadata).
    """
    df = pd.read_excel(path)
    if RESULT_COL in df.columns:
        df[RESULT_COL] = df[RESULT_COL].apply(_coerce_result)
        return df

    cols = number_columns or [c for c in df.columns if c not in _META_COLS]
    df[RESULT_COL] = df[cols].apply(lambda row: [int(v) for v in row if pd.notna(v)], axis=1)
    return df.drop(columns=cols)


_LOADERS = {
    ".jsonl": load_jsonl,
    ".json": load_jsonl,
    ".xlsx": load_excel,
    ".xls": load_excel,
}


def load_data(path, **kwargs) -> pd.DataFrame:
    """load draw data from ``path``, dispatching on file extension."""
    path = Path(path)
    loader = _LOADERS.get(path.suffix.lower())
    if loader is None:
        raise ValueError(f"unsupported data source '{path.suffix}', expected one of {sorted(_LOADERS)}")
    return loader(path, **kwargs)


def load_product(name: str, **kwargs) -> pd.DataFrame:
    """load a configured product by name using its ``raw_path``."""
    from vietlott.config.products import get_config

    return load_data(get_config(name).raw_path, **kwargs)
