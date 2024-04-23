# Vietlot data
## Predictions (just for testing, not a financial advice)
### random 10 tickets
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 8, 31, 43, 50, 53]   |
|   2 | [3, 8, 27, 35, 47, 51]   |
|   3 | [16, 20, 28, 45, 50, 52] |
|   4 | [4, 19, 29, 41, 44, 51]  |
|   5 | [3, 10, 14, 41, 48, 52]  |
|   6 | [4, 8, 32, 36, 39, 50]   |
|   7 | [3, 8, 40, 45, 49, 53]   |
|   8 | [5, 28, 32, 37, 47, 52]  |
|   9 | [10, 25, 31, 36, 44, 52] |
|  10 | [5, 18, 38, 44, 48, 52]  |

## raw details 6/55
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2024-04-23 | 01025 | [1, 34, 39, 40, 49, 53, 9]   |      0 | 2024-04-23 14:14:37.426346 |
| 2024-04-20 | 01024 | [2, 6, 35, 43, 45, 47, 14]   |      0 | 2024-04-20 14:12:50.026664 |
| 2024-04-18 | 01023 | [1, 21, 23, 33, 43, 54, 28]  |      0 | 2024-04-18 14:14:59.284531 |
| 2024-04-16 | 01022 | [3, 5, 32, 40, 46, 50, 37]   |      0 | 2024-04-16 14:15:40.685221 |
| 2024-04-13 | 01021 | [29, 36, 37, 38, 40, 42, 46] |      0 | 2024-04-13 14:13:37.096816 |
| 2024-04-11 | 01020 | [3, 6, 15, 25, 33, 43, 55]   |      0 | 2024-04-12 01:52:10.329864 |
| 2024-04-09 | 01019 | [4, 12, 27, 44, 46, 51, 22]  |      0 | 2024-04-09 14:14:57.731293 |
| 2024-04-06 | 01018 | [9, 13, 20, 30, 39, 54, 23]  |      0 | 2024-04-07 01:45:18.310035 |
| 2024-04-04 | 01017 | [3, 8, 12, 25, 47, 48, 15]   |      0 | 2024-04-04 14:08:08.988416 |
| 2024-04-02 | 01016 | [1, 12, 18, 20, 51, 52, 37]  |      0 | 2024-04-03 01:51:47.642083 |
## stats 6/55 all time
## stats 6/55 -15d
## stats 6/55 -30d
## stats 6/55 -60d
## stats 6/55 -90d

# Install
 
## run locally

```shell
# add PATH C:\Users\win\.pyenv\pyenv-win\versions\3.11.4\Scripts\
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

