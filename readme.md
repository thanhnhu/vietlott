# Vietlot
auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)
## Predictions (just for testing, not a financial advice)
### random 10 tickets of power 6/55

strategy 1:
| date       | result                  | predicted                |
|:-----------|:------------------------|:-------------------------|
| 2025-03-11 | [1, 16, 18, 30, 31, 44] | [16, 11, 18, 44, 34, 31] |
| 2024-03-26 | [1, 8, 13, 16, 38, 44]  | [44, 38, 13, 25, 16, 8]  |

strategy 2:
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [6, 12, 38, 41, 46, 55] |
|   2 | [3, 10, 13, 40, 49, 52] |

strategy 3:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [19, 26, 30, 37, 48, 52] |
|   2 | [12, 20, 24, 28, 43, 48] |
|   3 | [3, 18, 38, 44, 48, 51]  |
|   4 | [5, 23, 41, 48, 51, 54]  |
|   5 | [11, 21, 24, 47, 50, 53] |
|   6 | [4, 18, 22, 27, 34, 44]  |
|   7 | [8, 17, 21, 27, 44, 52]  |
|   8 | [10, 23, 38, 41, 45, 50] |
|   9 | [4, 10, 15, 44, 48, 53]  |
|  10 | [3, 29, 33, 36, 40, 44]  |

## top 20 details power 6/55
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2025-08-30 | 01236 | [2, 17, 19, 24, 30, 44]  |
| 2025-08-28 | 01235 | [6, 13, 28, 30, 35, 52]  |
| 2025-08-26 | 01234 | [22, 30, 38, 44, 48, 55] |
| 2025-08-23 | 01233 | [1, 9, 26, 34, 44, 50]   |
| 2025-08-21 | 01232 | [5, 9, 17, 35, 40, 41]   |
| 2025-08-19 | 01231 | [1, 14, 31, 34, 36, 47]  |
| 2025-08-16 | 01230 | [14, 23, 32, 36, 47, 48] |
| 2025-08-14 | 01229 | [6, 10, 17, 18, 32, 35]  |
| 2025-08-12 | 01228 | [1, 6, 24, 37, 40, 55]   |
| 2025-08-09 | 01227 | [5, 9, 16, 36, 43, 51]   |
| 2025-08-07 | 01226 | [6, 24, 31, 32, 39, 48]  |
| 2025-08-05 | 01225 | [8, 41, 45, 51, 52, 53]  |
| 2025-08-02 | 01224 | [12, 24, 29, 33, 34, 35] |
| 2025-07-31 | 01223 | [5, 17, 31, 42, 46, 49]  |
| 2025-07-29 | 01222 | [4, 8, 23, 43, 45, 51]   |
| 2025-07-26 | 01221 | [5, 26, 28, 29, 33, 54]  |
| 2025-07-24 | 01220 | [5, 10, 24, 29, 30, 34]  |
| 2025-07-22 | 01219 | [9, 10, 15, 28, 33, 44]  |
| 2025-07-19 | 01218 | [8, 9, 20, 36, 39, 44]   |
| 2025-07-17 | 01217 | [13, 18, 33, 40, 48, 53] |

### random 10 tickets of power 6/45

strategy 1:
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [6, 10, 16, 20, 40, 42] |
|   2 | [5, 19, 20, 21, 24, 40] |

strategy 2:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 15, 23, 27, 38, 42]  |
|   2 | [4, 15, 23, 30, 33, 37]  |
|   3 | [6, 12, 18, 37, 41, 43]  |
|   4 | [15, 18, 23, 26, 36, 42] |
|   5 | [5, 18, 23, 30, 40, 44]  |
|   6 | [5, 20, 25, 30, 40, 43]  |
|   7 | [9, 27, 30, 37, 40, 44]  |
|   8 | [7, 13, 17, 28, 40, 43]  |
|   9 | [10, 24, 30, 35, 38, 42] |
|  10 | [7, 18, 23, 27, 36, 42]  |

## top 20 details power 6/45
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2025-08-31 | 01400 | [3, 4, 14, 30, 32, 38]   |
| 2025-08-29 | 01399 | [2, 4, 10, 24, 35, 36]   |
| 2025-08-27 | 01398 | [3, 11, 18, 39, 40, 42]  |
| 2025-08-24 | 01397 | [2, 9, 20, 28, 32, 43]   |
| 2025-08-22 | 01396 | [1, 9, 10, 13, 37, 39]   |
| 2025-08-20 | 01395 | [4, 9, 27, 32, 38, 42]   |
| 2025-08-17 | 01394 | [15, 24, 26, 29, 31, 42] |
| 2025-08-15 | 01393 | [5, 22, 27, 36, 43, 45]  |
| 2025-08-13 | 01392 | [10, 15, 28, 30, 35, 45] |
| 2025-08-10 | 01391 | [13, 21, 26, 28, 31, 35] |
| 2025-08-08 | 01390 | [11, 17, 20, 26, 27, 38] |
| 2025-08-06 | 01389 | [3, 12, 14, 18, 29, 34]  |
| 2025-08-03 | 01388 | [5, 14, 24, 26, 37, 43]  |
| 2025-08-01 | 01387 | [5, 29, 30, 31, 36, 38]  |
| 2025-07-30 | 01386 | [2, 3, 6, 16, 26, 34]    |
| 2025-07-27 | 01385 | [1, 9, 12, 27, 39, 45]   |
| 2025-07-25 | 01384 | [20, 30, 34, 35, 38, 39] |
| 2025-07-23 | 01383 | [24, 26, 29, 32, 37, 44] |
| 2025-07-20 | 01382 | [11, 13, 14, 20, 37, 42] |
| 2025-07-18 | 01381 | [7, 22, 24, 28, 42, 45]  |

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

