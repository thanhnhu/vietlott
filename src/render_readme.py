# /usr/bin/env python
from datetime import datetime, timedelta
from io import StringIO
from pathlib import Path

import pandas as pd
from loguru import logger

from vietlott.config.products import get_config
from vietlott.model.strategy.random import RandomModel
from vietlott.predictor.predictor import Predictor

include_install_section = """# Install
 
## run locally

```shell
# add PATH C:\\Users\\win\\.pyenv\\pyenv-win\\versions\\3.11.4\\Scripts\\
$ pip install -r requirements.txt
$ python src/vietlott/cli/crawl.py power_655
$ python src/vietlott/cli/missing.py power_655
$ python src/render_readme.py
$ python src/vietlott/predictor/predictor.py
```
 
## via pip

```shell
pip install -i https://test.pypi.org/simple/ vietlott-data==0.1.2
```

## cli
project provides two cli

### crawl
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

### Backfill missing data

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


def main():
    df = pd.read_json(get_config("power_655").raw_path, lines=True, dtype=object, convert_dates=False)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    df = df.sort_values(by=["date", "id"], ascending=False)

    df_645 = pd.read_json(get_config("power_645").raw_path, lines=True, dtype=object, convert_dates=False)
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
    # strategy 1
    random_model = RandomModel(df, ticket_per_days)
    random_model.backtest()
    random_model.evaluate()
    df_random_correct = random_model.df_backtest_evaluate[random_model.df_backtest_evaluate["correct_num"] >= 5][
        ["date", "result", "predicted"]
    ]
    # strategy 2
    df_random_tickets_655 = Predictor().predict(df, ticket_per_days)
    df_random_tickets_655 = pd.DataFrame({'#': range(1, len(df_random_tickets_655) + 1),
                                      'Tickets': df_random_tickets_655.values.tolist()})

    df_random_tickets_645 = Predictor().predict(df_645, ticket_per_days)
    df_random_tickets_645 = pd.DataFrame({'#': range(1, len(df_random_tickets_645) + 1),
                                      'Tickets': df_random_tickets_645.values.tolist()})

    output_str = f"""# Vietlot
auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)
## Predictions (just for testing, not a financial advice)
### random 10 tickets of power 6/55

strategy 1:
{df_random_correct.to_markdown(index=False)}

strategy 2:
{df_random_tickets_655.to_markdown(index=False)}

## top 20 details power 6/55
{df.drop(['page', 'process_time'], axis=1).head(20).to_markdown(index=False)}

### random 10 tickets of power 6/45
{df_random_tickets_645.to_markdown(index=False)}

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
