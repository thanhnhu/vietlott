# Vietlot
auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)
## Predictions (just for testing, not a financial advice)
### random 10 tickets of power 6/55

strategy 1:
| date       | result                   | predicted               |
|:-----------|:-------------------------|:------------------------|
| 2023-11-07 | [12, 18, 20, 28, 35, 52] | [3, 20, 52, 18, 25, 35] |

strategy 2:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [18, 26, 38, 39, 47, 51] |
|   2 | [13, 16, 32, 33, 35, 43] |

strategy 3:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [6, 10, 36, 42, 50, 54]  |
|   2 | [7, 11, 16, 21, 38, 51]  |
|   3 | [22, 32, 36, 41, 45, 49] |
|   4 | [4, 21, 27, 30, 46, 53]  |
|   5 | [3, 32, 39, 43, 48, 52]  |
|   6 | [11, 16, 20, 31, 46, 50] |
|   7 | [3, 9, 23, 27, 37, 51]   |
|   8 | [14, 19, 25, 48, 51, 54] |
|   9 | [3, 14, 26, 36, 47, 53]  |
|  10 | [3, 7, 14, 38, 42, 51]   |

## top 20 details power 6/55
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2026-02-05 | 01304 | [7, 13, 16, 25, 26, 55]  |
| 2026-02-03 | 01303 | [12, 15, 18, 22, 48, 53] |
| 2026-01-31 | 01302 | [10, 11, 14, 17, 49, 53] |
| 2026-01-29 | 01301 | [11, 15, 22, 32, 34, 54] |
| 2026-01-27 | 01300 | [13, 22, 32, 42, 53, 54] |
| 2026-01-24 | 01299 | [14, 24, 25, 30, 35, 53] |
| 2026-01-22 | 01298 | [2, 20, 21, 29, 36, 50]  |
| 2026-01-20 | 01297 | [4, 20, 26, 28, 37, 41]  |
| 2026-01-17 | 01296 | [14, 21, 23, 25, 46, 48] |
| 2026-01-15 | 01295 | [13, 21, 31, 34, 48, 55] |
| 2026-01-13 | 01294 | [3, 12, 25, 51, 52, 55]  |
| 2026-01-10 | 01293 | [9, 16, 30, 33, 34, 38]  |
| 2026-01-08 | 01292 | [20, 22, 36, 43, 45, 50] |
| 2026-01-06 | 01291 | [22, 28, 29, 30, 34, 47] |
| 2026-01-03 | 01290 | [10, 16, 17, 23, 33, 36] |
| 2026-01-01 | 01289 | [5, 16, 29, 33, 39, 42]  |
| 2025-12-30 | 01288 | [11, 30, 35, 41, 48, 55] |
| 2025-12-27 | 01287 | [16, 21, 30, 37, 39, 40] |
| 2025-12-25 | 01286 | [4, 6, 32, 37, 40, 48]   |
| 2025-12-23 | 01285 | [2, 10, 16, 25, 32, 38]  |

### random 10 tickets of power 6/45

strategy 1:
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [8, 12, 17, 23, 26, 27] |
|   2 | [3, 7, 11, 16, 19, 35]  |

strategy 2:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [5, 18, 31, 37, 41, 44]  |
|   2 | [4, 20, 23, 27, 40, 44]  |
|   3 | [9, 14, 18, 28, 33, 37]  |
|   4 | [12, 18, 23, 36, 40, 43] |
|   5 | [8, 15, 23, 37, 41, 44]  |
|   6 | [3, 8, 22, 27, 40, 43]   |
|   7 | [9, 14, 26, 34, 40, 43]  |
|   8 | [3, 8, 32, 38, 42, 44]   |
|   9 | [4, 15, 30, 35, 40, 43]  |
|  10 | [16, 20, 23, 27, 39, 42] |

## top 20 details power 6/45
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2026-02-01 | 01466 | [1, 18, 21, 23, 30, 36]  |
| 2026-01-30 | 01465 | [16, 17, 30, 41, 42, 45] |
| 2026-01-28 | 01464 | [4, 10, 16, 19, 27, 40]  |
| 2026-01-25 | 01463 | [2, 19, 20, 24, 33, 34]  |
| 2026-01-23 | 01462 | [9, 15, 16, 20, 22, 31]  |
| 2026-01-21 | 01461 | [1, 18, 23, 24, 29, 37]  |
| 2026-01-18 | 01460 | [2, 5, 15, 26, 39, 42]   |
| 2026-01-16 | 01459 | [2, 10, 21, 31, 34, 40]  |
| 2026-01-14 | 01458 | [1, 22, 23, 28, 39, 45]  |
| 2026-01-11 | 01457 | [8, 10, 21, 25, 31, 38]  |
| 2026-01-09 | 01456 | [8, 9, 17, 21, 36, 45]   |
| 2026-01-07 | 01455 | [1, 5, 7, 28, 31, 43]    |
| 2026-01-04 | 01454 | [2, 12, 21, 29, 35, 44]  |
| 2026-01-02 | 01453 | [7, 18, 22, 32, 37, 38]  |
| 2025-12-31 | 01452 | [1, 25, 35, 36, 37, 45]  |
| 2025-12-28 | 01451 | [1, 2, 7, 16, 31, 37]    |
| 2025-12-26 | 01450 | [4, 6, 16, 25, 27, 40]   |
| 2025-12-24 | 01449 | [15, 19, 31, 35, 43, 45] |
| 2025-12-21 | 01448 | [6, 9, 12, 18, 29, 43]   |
| 2025-12-19 | 01447 | [1, 21, 36, 42, 43, 44]  |

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
$ python src/vietlott/predictor/predictor2.py
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

