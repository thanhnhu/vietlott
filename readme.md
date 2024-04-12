# Vietlot data
## Predictions (just for testing, not a financial advice)
### random 10 tickets
|   0 |   1 |   2 |   3 |   4 |   5 |
|----:|----:|----:|----:|----:|----:|
|   3 |   9 |  22 |  29 |  45 |  52 |
|   3 |  11 |  25 |  41 |  45 |  49 |
|   4 |   8 |  16 |  22 |  44 |  52 |
|   4 |  11 |  28 |  34 |  46 |  50 |
|   4 |  10 |  31 |  44 |  50 |  53 |
|   3 |   9 |  26 |  30 |  41 |  47 |
|   4 |   8 |  25 |  31 |  45 |  49 |
|   6 |  28 |  35 |  42 |  46 |  52 |
|   4 |  20 |  38 |  43 |  46 |  51 |
|   4 |  11 |  28 |  34 |  44 |  52 |

## raw details 6/55
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2024-04-11 | 01020 | [3, 6, 15, 25, 33, 43, 55]   |      0 | 2024-04-12 01:52:10.329864 |
| 2024-04-09 | 01019 | [4, 12, 27, 44, 46, 51, 22]  |      0 | 2024-04-09 14:14:57.731293 |
| 2024-04-06 | 01018 | [9, 13, 20, 30, 39, 54, 23]  |      0 | 2024-04-07 01:45:18.310035 |
| 2024-04-04 | 01017 | [3, 8, 12, 25, 47, 48, 15]   |      0 | 2024-04-04 14:08:08.988416 |
| 2024-04-02 | 01016 | [1, 12, 18, 20, 51, 52, 37]  |      0 | 2024-04-03 01:51:47.642083 |
| 2024-03-30 | 01015 | [14, 17, 27, 38, 54, 55, 23] |      0 | 2024-03-31 01:55:34.015736 |
| 2024-03-28 | 01014 | [1, 7, 18, 26, 38, 49, 21]   |      0 | 2024-03-29 01:49:59.328787 |
| 2024-03-26 | 01013 | [1, 8, 13, 16, 38, 44, 47]   |      0 | 2024-03-27 01:50:40.849831 |
| 2024-03-23 | 01012 | [3, 10, 13, 30, 40, 52, 4]   |      0 | 2024-03-24 01:55:49.474576 |
| 2024-03-21 | 01011 | [12, 13, 41, 48, 49, 53, 43] |      0 | 2024-03-22 01:49:41.601528 |
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

