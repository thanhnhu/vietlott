# Vietlot
auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)
## Predictions (just for testing, not a financial advice)
### random 10 tickets of power 6/55

strategy 1:
| date       | result                  | predicted               |
|:-----------|:------------------------|:------------------------|
| 2023-06-13 | [4, 14, 18, 27, 47, 50] | [50, 14, 4, 37, 27, 18] |

strategy 2:
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [1, 2, 14, 32, 33, 41]  |
|   2 | [8, 12, 42, 47, 51, 52] |

strategy 3:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [25, 32, 43, 47, 50, 53] |
|   2 | [3, 7, 15, 41, 49, 53]   |
|   3 | [7, 15, 32, 37, 43, 50]  |
|   4 | [7, 29, 37, 42, 48, 52]  |
|   5 | [12, 31, 35, 42, 46, 52] |
|   6 | [8, 37, 42, 47, 50, 52]  |
|   7 | [7, 16, 22, 39, 44, 48]  |
|   8 | [10, 15, 18, 27, 46, 52] |
|   9 | [6, 19, 32, 40, 46, 52]  |
|  10 | [4, 8, 31, 36, 39, 47]   |

## top 20 details power 6/55
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
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
| 2025-12-20 | 01284 | [22, 32, 33, 35, 40, 41] |
| 2025-12-18 | 01283 | [12, 14, 29, 30, 39, 55] |
| 2025-12-16 | 01282 | [7, 36, 37, 38, 52, 55]  |
| 2025-12-13 | 01281 | [5, 8, 12, 18, 20, 38]   |
| 2025-12-11 | 01280 | [9, 13, 21, 45, 48, 55]  |
| 2025-12-09 | 01279 | [14, 21, 26, 27, 31, 43] |
| 2025-12-06 | 01278 | [12, 26, 34, 37, 50, 52] |
| 2025-12-04 | 01277 | [10, 29, 32, 33, 44, 53] |
| 2025-12-02 | 01276 | [16, 20, 24, 36, 51, 54] |

### random 10 tickets of power 6/45

strategy 1:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [15, 19, 24, 25, 27, 39] |
|   2 | [4, 5, 28, 32, 37, 42]   |

strategy 2:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [2, 12, 23, 27, 30, 36]  |
|   2 | [11, 17, 22, 26, 40, 43] |
|   3 | [3, 11, 17, 22, 34, 42]  |
|   4 | [7, 10, 16, 21, 36, 44]  |
|   5 | [8, 12, 19, 29, 40, 43]  |
|   6 | [14, 20, 24, 29, 32, 41] |
|   7 | [10, 24, 27, 30, 39, 43] |
|   8 | [4, 14, 30, 35, 38, 43]  |
|   9 | [3, 15, 23, 26, 36, 43]  |
|  10 | [5, 11, 24, 35, 40, 43]  |

## top 20 details power 6/45
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
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
| 2025-12-17 | 01446 | [5, 14, 24, 38, 41, 43]  |
| 2025-12-14 | 01445 | [8, 11, 13, 16, 28, 32]  |
| 2025-12-12 | 01444 | [3, 7, 13, 17, 38, 44]   |
| 2025-12-10 | 01443 | [7, 18, 22, 29, 30, 36]  |
| 2025-12-07 | 01442 | [1, 5, 23, 28, 29, 43]   |
| 2025-12-05 | 01441 | [2, 19, 23, 37, 42, 43]  |

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

