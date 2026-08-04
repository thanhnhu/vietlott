# /usr/bin/env python
from datetime import datetime, timedelta
from io import StringIO
from pathlib import Path

import pandas as pd
from loguru import logger

from vietlott.config.products import get_config
from vietlott.datasource import load_product
from vietlott.model.strategy.random import RandomStrategy
from vietlott.model.strategy.frequency import FrequencyStrategy
from vietlott.model.strategy.random_forest import RandomForestStrategy
from vietlott.model.strategy.lstm import LSTMStrategy

include_install_section = """## Install

### run locally

```shell
pip install -r requirements.txt
pip install -e .[ml]  # optional: enables RandomForest / LSTM strategies
python src/vietlott/cli/crawl.py power_655
python src/vietlott/cli/missing.py power_655
python src/render_readme.py
python src/vietlott/model/strategy/random_forest.py
python src/vietlott/model/strategy/lstm.py
```

### via pip

```shell
pip install -i https://test.pypi.org/simple/ vietlott-data==0.1.2
```

### cli

project provides two cli

#### crawl

```shell
Usage: vietlott-crawl [OPTIONS] PRODUCT

  crawl a product with a given run date or from/to index page :param ctx:
  :param product: :param run_date: :param index_from: :param index_to:
  :return:

Options:
  --run-date TEXT
  --index_from INTEGER  page index from run since we crawl by pagination the
                        pages
  --index_to INTEGER    page index from run since we crawl by pagination the
                        pages
  --help                Show this message and exit.
```

#### Backfill missing data

```shell
Usage: vietlott-missing [OPTIONS] PRODUCT

  detect_missing_data and run if needed :param ctx: context :param product:
  product to run :param limit: number of pages to run :return:

Options:
  --limit INTEGER
  --help           Show this message and exit.
```
"""


def _balance_long_df(df_: pd.DataFrame, n_splits: int = 20):
    """convert long dataframe to multiple columns"""
    df_ = df_.reset_index()
    df_["result"] = df_["result"].astype(str)
    df_["count"] = df_["count"].astype(str)

    final = None

    for i in range(len(df_) // n_splits + 1):
        dd = df_.iloc[i * n_splits : (i + 1) * n_splits]

        if final is None:
            final = dd
        else:
            final = pd.concat(
                [
                    final.reset_index(drop=True),
                    pd.DataFrame([None] * len(dd), columns=["-"]),
                    dd.reset_index(drop=True),
                ],
                axis="columns",
            )
    final = final.fillna("")

    return final


def read_data(data_dir: Path):
    df_files = [
        pd.read_json(str(file), dtype=False, convert_dates=False, lines=True) for file in data_dir.glob("*.jsonl")
    ]
    logger.info("df_files: %d", len(df_files))
    logger.info(df_files[0])
    df = pd.concat(df_files, axis="rows")
    return df


def read_data_str(data_dir: Path):
    string = ""
    for file in data_dir.glob("*.jsonl"):
        string += file.open("r").read()
    df = pd.read_json(StringIO(string), lines=True, dtype=object, convert_dates=False)
    return df


def _tickets_table(label: str, factory, n: int) -> pd.DataFrame:
    """build a '#/Tickets' table, degrading gracefully if optional ml deps are missing."""
    try:
        tickets = factory().generate(n=n)
    except ImportError as exc:
        logger.warning(f"skipping {label}: {exc}")
        return pd.DataFrame({"Tickets": ["(requires optional 'ml' extra: pip install vietlott-data[ml])"]})
    return pd.DataFrame({"#": range(1, len(tickets) + 1), "Tickets": tickets})


def main():
    df_655 = load_product("power_655")
    df_655["date"] = pd.to_datetime(df_655["date"]).dt.date
    df_655 = df_655.sort_values(by=["date", "id"], ascending=False)

    df_645 = load_product("power_645")
    df_645["date"] = pd.to_datetime(df_645["date"]).dt.date
    df_645 = df_645.sort_values(by=["date", "id"], ascending=False)

    def fn_stats(df_):
        df_explode = df_.explode("result")
        stats = df_explode.groupby("result").agg(count=("id", "count"))
        stats["%"] = (stats["count"] / len(df_explode) * 100).round(2)
        return stats

    #stats = _balance_long_df(fn_stats(df))

    # stats n months
    #stats_15d = _balance_long_df(fn_stats(df[df["date"] >= (datetime.now().date() - timedelta(days=15))]))
    #stats_30d = _balance_long_df(fn_stats(df[df["date"] >= (datetime.now().date() - timedelta(days=30))]))
    #stats_60d = _balance_long_df(fn_stats(df[df["date"] >= (datetime.now().date() - timedelta(days=60))]))
    #stats_90d = _balance_long_df(fn_stats(df[df["date"] >= (datetime.now().date() - timedelta(days=90))]))

    # predictions
    ticket_per_days = 10
    cfg_655 = get_config("power_655")
    cfg_645 = get_config("power_645")
    # strategy 1: uniform baseline, showing backtest hits (>=5 correct)
    random_model = RandomStrategy(df_655, ticket_per_days)
    random_model.backtest()
    random_model.evaluate()
    table_655_random = random_model.df_backtest_evaluate[random_model.df_backtest_evaluate["correct_num"] >= 5][["date", "result", "predicted"]]
    # strategy 2: LSTM (optional ml extra)
    table_655_lstm = _tickets_table(
        "lstm 6/55", lambda: LSTMStrategy(df_655, min_val=cfg_655.min_value, max_val=cfg_655.max_value), 2
    )
    table_645_lstm = _tickets_table(
        "lstm 6/45", lambda: LSTMStrategy(df_645, min_val=cfg_645.min_value, max_val=cfg_645.max_value), 2
    )
    # strategy 3: RandomForest (optional ml extra)
    table_655_random_forest = _tickets_table(
        "random_forest 6/55",
        lambda: RandomForestStrategy(df_655, min_val=cfg_655.min_value, max_val=cfg_655.max_value),
        ticket_per_days,
    )
    table_645_random_forest = _tickets_table(
        "random_forest 6/45",
        lambda: RandomForestStrategy(df_645, min_val=cfg_645.min_value, max_val=cfg_645.max_value),
        ticket_per_days,
    )
    # strategy 4: frequency-weighted, shaped to historical distribution
    table_655_frequency = _tickets_table(
        "frequency 6/55",
        lambda: FrequencyStrategy(df_655, min_val=cfg_655.min_value, max_val=cfg_655.max_value),
        ticket_per_days,
    )
    table_645_frequency = _tickets_table(
        "frequency 6/45",
        lambda: FrequencyStrategy(df_645, min_val=cfg_645.min_value, max_val=cfg_645.max_value),
        ticket_per_days,
    )

    output_str = f"""# Vietlott

auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)

## Predictions (just for testing, not a financial advice)

### random 10 tickets of power 6/55

strategy 1:
{table_655_random.to_markdown(index=False)}

strategy 2:
{table_655_lstm.to_markdown(index=False)}

strategy 3:
{table_655_random_forest.to_markdown(index=False)}

strategy 4 (frequency-weighted):
{table_655_frequency.to_markdown(index=False)}

## top 20 details power 6/55
{df_655.drop(['page', 'process_time'], axis=1).head(20).to_markdown(index=False)}

### random 10 tickets of power 6/45

strategy 1:
{table_645_lstm.to_markdown(index=False)}

strategy 2:
{table_645_random_forest.to_markdown(index=False)}

strategy 3 (frequency-weighted):
{table_645_frequency.to_markdown(index=False)}

## top 20 details power 6/45
{df_645.drop(['page', 'process_time'], axis=1).head(20).to_markdown(index=False)}

<!---
stats 6/55 all time - stats.to_markdown(index=False)
stats 6/55 -15d - stats_15d.to_markdown(index=False)
stats 6/55 -30d - stats_30d.to_markdown(index=False)
stats 6/55 -60d - stats_60d.to_markdown(index=False)
stats 6/55 -90d - stats_90d.to_markdown(index=False)
-->

{include_install_section}
"""
    path_output = Path("./readme.md")
    with path_output.open("w") as ofile:
        logger.info(f"cwd: {Path.cwd()}")
        logger.info(f"writing to {path_output.absolute()}")
        ofile.write(output_str)


if __name__ == "__main__":
    main()
