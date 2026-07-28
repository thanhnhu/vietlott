# Vietlot
auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)
## Predictions (just for testing, not a financial advice)
### random 10 tickets of power 6/55

strategy 1:
| date       | result                  | predicted               |
|:-----------|:------------------------|:------------------------|
| 2025-05-29 | [9, 37, 42, 45, 46, 50] | [6, 45, 46, 37, 9, 14]  |
| 2019-06-29 | [6, 10, 19, 31, 34, 43] | [34, 6, 10, 42, 43, 31] |

strategy 2:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [9, 22, 31, 39, 43, 51]  |
|   2 | [15, 21, 23, 26, 31, 43] |

strategy 3:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 24, 30, 40, 45, 51]  |
|   2 | [4, 13, 25, 44, 48, 52]  |
|   3 | [11, 18, 21, 27, 44, 52] |
|   4 | [3, 10, 31, 41, 45, 52]  |
|   5 | [4, 22, 37, 43, 46, 52]  |
|   6 | [7, 14, 21, 45, 49, 53]  |
|   7 | [18, 31, 36, 45, 49, 53] |
|   8 | [21, 25, 33, 41, 45, 52] |
|   9 | [7, 15, 21, 35, 39, 43]  |
|  10 | [6, 12, 31, 37, 47, 52]  |

## top 20 details power 6/55
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2026-07-28 | 01377 | [7, 22, 23, 27, 41, 44]  |
| 2026-07-25 | 01376 | [5, 9, 27, 33, 37, 50]   |
| 2026-07-23 | 01375 | [1, 3, 8, 38, 40, 55]    |
| 2026-07-21 | 01374 | [8, 11, 22, 24, 32, 39]  |
| 2026-07-18 | 01373 | [22, 41, 45, 48, 54, 55] |
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

### random 10 tickets of power 6/45

strategy 1:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [1, 2, 3, 11, 25, 37]    |
|   2 | [11, 15, 18, 27, 34, 37] |

strategy 2:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [17, 24, 27, 30, 33, 39] |
|   2 | [4, 12, 17, 23, 40, 43]  |
|   3 | [4, 8, 31, 37, 42, 44]   |
|   4 | [16, 23, 29, 38, 41, 44] |
|   5 | [6, 17, 23, 38, 42, 44]  |
|   6 | [4, 11, 25, 30, 35, 42]  |
|   7 | [4, 14, 29, 34, 40, 43]  |
|   8 | [3, 6, 13, 36, 40, 43]   |
|   9 | [5, 9, 12, 20, 40, 43]   |
|  10 | [3, 8, 23, 36, 40, 43]   |

## top 20 details power 6/45
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2026-07-26 | 01541 | [13, 16, 27, 33, 41, 44] |
| 2026-07-24 | 01540 | [12, 16, 36, 38, 41, 45] |
| 2026-07-22 | 01539 | [3, 32, 33, 34, 39, 43]  |
| 2026-07-19 | 01538 | [12, 22, 24, 26, 31, 37] |
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

