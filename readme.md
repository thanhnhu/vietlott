# Vietlot
auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)
## Predictions (just for testing, not a financial advice)
### random 10 tickets of power 6/55

strategy 1:
| date       | result                   | predicted               |
|:-----------|:-------------------------|:------------------------|
| 2018-11-15 | [13, 16, 21, 40, 49, 52] | [54, 21, 16, 6, 13, 52] |

strategy 2:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 12, 22, 41, 46, 52]  |
|   2 | [15, 19, 27, 34, 43, 52] |
|   3 | [7, 10, 16, 20, 49, 53]  |
|   4 | [11, 15, 29, 35, 49, 53] |
|   5 | [3, 19, 29, 39, 42, 49]  |
|   6 | [4, 29, 32, 35, 41, 47]  |
|   7 | [6, 27, 43, 48, 50, 54]  |
|   8 | [2, 9, 14, 42, 49, 52]   |
|   9 | [4, 23, 38, 46, 48, 53]  |
|  10 | [4, 10, 13, 31, 46, 51]  |

## top 20 details power 6/55
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2025-01-09 | 01137 | [18, 21, 31, 39, 50, 53] |
| 2025-01-07 | 01136 | [4, 5, 9, 16, 22, 39]    |
| 2025-01-04 | 01135 | [4, 10, 30, 36, 40, 53]  |
| 2025-01-02 | 01134 | [4, 10, 18, 22, 41, 45]  |
| 2024-12-31 | 01133 | [8, 13, 29, 36, 42, 43]  |
| 2024-12-28 | 01132 | [6, 19, 36, 42, 53, 55]  |
| 2024-12-26 | 01131 | [6, 18, 33, 38, 41, 48]  |
| 2024-12-24 | 01130 | [17, 20, 27, 32, 44, 51] |
| 2024-12-21 | 01129 | [4, 16, 29, 30, 35, 51]  |
| 2024-12-19 | 01128 | [13, 16, 32, 39, 49, 51] |
| 2024-12-17 | 01127 | [2, 14, 27, 30, 53, 54]  |
| 2024-12-14 | 01126 | [3, 10, 19, 20, 21, 24]  |
| 2024-12-12 | 01125 | [1, 9, 12, 18, 37, 44]   |
| 2024-12-10 | 01124 | [11, 15, 26, 45, 52, 55] |
| 2024-12-07 | 01123 | [16, 17, 22, 24, 29, 37] |
| 2024-12-05 | 01122 | [16, 21, 29, 41, 42, 47] |
| 2024-12-03 | 01121 | [10, 19, 33, 39, 47, 54] |
| 2024-11-30 | 01120 | [1, 20, 24, 26, 38, 41]  |
| 2024-11-28 | 01119 | [1, 16, 24, 28, 38, 53]  |
| 2024-11-26 | 01118 | [8, 11, 16, 32, 40, 43]  |

### random 10 tickets of power 6/45
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [6, 16, 25, 33, 38, 43]  |
|   2 | [4, 12, 17, 29, 38, 43]  |
|   3 | [8, 11, 14, 20, 24, 43]  |
|   4 | [3, 18, 22, 24, 39, 42]  |
|   5 | [14, 20, 32, 37, 40, 43] |
|   6 | [10, 21, 28, 32, 37, 43] |
|   7 | [5, 20, 34, 38, 40, 44]  |
|   8 | [9, 18, 23, 35, 40, 44]  |
|   9 | [4, 12, 32, 37, 41, 44]  |
|  10 | [6, 24, 28, 32, 35, 43]  |

## top 20 details power 6/45
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2025-01-10 | 01301 | [2, 4, 8, 28, 42, 44]    |
| 2025-01-08 | 01300 | [2, 3, 17, 33, 37, 38]   |
| 2025-01-05 | 01299 | [2, 7, 15, 37, 41, 42]   |
| 2025-01-03 | 01298 | [6, 12, 21, 27, 34, 41]  |
| 2025-01-01 | 01297 | [14, 20, 25, 28, 36, 40] |
| 2024-12-29 | 01296 | [5, 8, 19, 31, 34, 43]   |
| 2024-12-27 | 01295 | [1, 10, 13, 24, 25, 33]  |
| 2024-12-25 | 01294 | [8, 13, 20, 25, 28, 39]  |
| 2024-12-22 | 01293 | [15, 16, 24, 27, 31, 44] |
| 2024-12-20 | 01292 | [6, 9, 12, 21, 28, 33]   |
| 2024-12-18 | 01291 | [3, 7, 12, 16, 26, 34]   |
| 2024-12-15 | 01290 | [1, 10, 20, 22, 23, 36]  |
| 2024-12-13 | 01289 | [3, 7, 29, 36, 37, 44]   |
| 2024-12-11 | 01288 | [2, 10, 17, 23, 29, 33]  |
| 2024-12-08 | 01287 | [1, 13, 24, 26, 27, 37]  |
| 2024-12-06 | 01286 | [8, 14, 18, 26, 34, 42]  |
| 2024-12-04 | 01285 | [7, 14, 19, 24, 34, 36]  |
| 2024-12-01 | 01284 | [15, 17, 25, 29, 33, 35] |
| 2024-11-29 | 01283 | [12, 15, 33, 35, 37, 45] |
| 2024-11-27 | 01282 | [6, 21, 24, 31, 42, 44]  |

<!---
stats 6/55 all time - stats.to_markdown(index=False)
stats 6/55 -15d - stats_15d.to_markdown(index=False)
stats 6/55 -30d - stats_30d.to_markdown(index=False)
stats 6/55 -60d - stats_60d.to_markdown(index=False)
stats 6/55 -90d - stats_90d.to_markdown(index=False)
-->

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

