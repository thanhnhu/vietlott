# Vietlot
auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)
## Predictions (just for testing, not a financial advice)
### random 10 tickets of power 6/55

strategy 1:
| date       | result                   | predicted                |
|:-----------|:-------------------------|:-------------------------|
| 2025-12-04 | [10, 29, 32, 33, 44, 53] | [10, 29, 4, 33, 14, 53]  |
| 2021-04-27 | [3, 9, 22, 26, 32, 37]   | [32, 22, 26, 41, 9, 20]  |
| 2018-05-08 | [3, 16, 23, 24, 38, 42]  | [42, 23, 48, 27, 24, 38] |

strategy 2:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 5, 6, 29, 32, 44]    |
|   2 | [29, 34, 35, 38, 50, 51] |

strategy 3:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 24, 37, 44, 48, 53]  |
|   2 | [18, 23, 29, 40, 45, 52] |
|   3 | [4, 32, 37, 41, 50, 53]  |
|   4 | [4, 25, 31, 43, 49, 54]  |
|   5 | [10, 19, 29, 42, 48, 53] |
|   6 | [4, 16, 23, 46, 51, 54]  |
|   7 | [13, 17, 30, 34, 38, 43] |
|   8 | [18, 22, 39, 42, 49, 53] |
|   9 | [10, 19, 26, 41, 47, 51] |
|  10 | [5, 11, 16, 20, 44, 49]  |

## top 20 details power 6/55
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2026-07-16 | 01372 | [19, 20, 33, 45, 48, 53] |
| 2026-07-14 | 01371 | [10, 24, 30, 35, 45, 51] |
| 2026-07-11 | 01370 | [9, 17, 20, 33, 41, 42]  |
| 2026-07-09 | 01369 | [2, 9, 10, 14, 17, 49]   |
| 2026-07-07 | 01368 | [4, 6, 25, 32, 33, 44]   |
| 2026-07-04 | 01367 | [13, 15, 18, 23, 31, 43] |
| 2026-07-02 | 01366 | [5, 11, 28, 34, 41, 42]  |
| 2026-06-30 | 01365 | [5, 13, 18, 22, 43, 44]  |
| 2026-06-27 | 01364 | [7, 16, 21, 23, 28, 52]  |
| 2026-06-25 | 01363 | [1, 3, 8, 15, 35, 55]    |
| 2026-06-23 | 01362 | [1, 13, 28, 38, 40, 46]  |
| 2026-06-20 | 01361 | [16, 23, 26, 30, 52, 53] |
| 2026-06-18 | 01360 | [1, 4, 14, 20, 46, 49]   |
| 2026-06-16 | 01359 | [2, 4, 5, 7, 31, 40]     |
| 2026-06-13 | 01358 | [2, 8, 19, 33, 36, 47]   |
| 2026-06-11 | 01357 | [1, 8, 17, 24, 40, 48]   |
| 2026-06-09 | 01356 | [6, 8, 18, 27, 32, 34]   |
| 2026-06-06 | 01355 | [3, 11, 16, 37, 39, 41]  |
| 2026-06-04 | 01354 | [23, 24, 28, 29, 39, 43] |
| 2026-06-02 | 01353 | [1, 3, 5, 16, 37, 51]    |

### random 10 tickets of power 6/45

strategy 1:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 13, 20, 29, 32, 37]  |
|   2 | [20, 22, 23, 32, 35, 40] |

strategy 2:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 7, 18, 28, 33, 40]   |
|   2 | [5, 21, 25, 35, 39, 43]  |
|   3 | [3, 11, 23, 37, 40, 44]  |
|   4 | [4, 8, 32, 37, 40, 43]   |
|   5 | [4, 19, 30, 37, 39, 43]  |
|   6 | [3, 12, 33, 39, 42, 44]  |
|   7 | [11, 16, 19, 38, 41, 44] |
|   8 | [10, 19, 33, 38, 42, 44] |
|   9 | [14, 23, 26, 33, 40, 43] |
|  10 | [5, 21, 24, 28, 31, 43]  |

## top 20 details power 6/45
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2026-07-17 | 01537 | [9, 18, 30, 31, 39, 45]  |
| 2026-07-15 | 01536 | [7, 11, 29, 37, 43, 45]  |
| 2026-07-12 | 01535 | [6, 9, 11, 17, 35, 44]   |
| 2026-07-10 | 01534 | [9, 17, 23, 26, 42, 44]  |
| 2026-07-08 | 01533 | [13, 14, 22, 26, 37, 44] |
| 2026-07-05 | 01532 | [1, 5, 13, 29, 32, 35]   |
| 2026-07-03 | 01531 | [6, 20, 21, 28, 30, 39]  |
| 2026-07-01 | 01530 | [20, 24, 25, 29, 40, 44] |
| 2026-06-28 | 01529 | [2, 11, 18, 33, 42, 45]  |
| 2026-06-26 | 01528 | [9, 14, 31, 36, 41, 45]  |
| 2026-06-24 | 01527 | [3, 11, 17, 19, 30, 32]  |
| 2026-06-21 | 01526 | [3, 8, 19, 27, 41, 45]   |
| 2026-06-19 | 01525 | [6, 9, 19, 29, 30, 36]   |
| 2026-06-17 | 01524 | [5, 6, 16, 28, 35, 39]   |
| 2026-06-14 | 01523 | [7, 16, 20, 22, 24, 38]  |
| 2026-06-12 | 01522 | [5, 15, 30, 34, 37, 38]  |
| 2026-06-10 | 01521 | [3, 9, 17, 22, 27, 32]   |
| 2026-06-07 | 01520 | [14, 21, 26, 30, 34, 35] |
| 2026-06-05 | 01519 | [13, 16, 19, 32, 36, 39] |
| 2026-06-03 | 01518 | [3, 11, 26, 33, 36, 38]  |

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

