# Vietlot
auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)
## Predictions (just for testing, not a financial advice)
### random 10 tickets of power 6/55

strategy 1:
| date       | result                   | predicted                |
|:-----------|:-------------------------|:-------------------------|
| 2022-05-17 | [11, 17, 25, 29, 45, 48] | [29, 17, 25, 53, 48, 42] |

strategy 2:
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [1, 21, 23, 33, 43, 54] |
|   2 | [2, 6, 35, 43, 45, 47]  |

strategy 3:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [6, 29, 34, 39, 48, 53]  |
|   2 | [2, 14, 21, 35, 49, 54]  |
|   3 | [9, 15, 21, 44, 49, 52]  |
|   4 | [20, 36, 41, 44, 48, 53] |
|   5 | [12, 28, 35, 45, 50, 53] |
|   6 | [2, 7, 27, 32, 48, 52]   |
|   7 | [8, 26, 31, 36, 48, 53]  |
|   8 | [4, 27, 38, 44, 49, 53]  |
|   9 | [10, 20, 25, 35, 48, 52] |
|  10 | [22, 32, 40, 46, 49, 52] |

## top 20 details power 6/55
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2025-12-06 | 01278 | [12, 26, 34, 37, 50, 52] |
| 2025-12-04 | 01277 | [10, 29, 32, 33, 44, 53] |
| 2025-12-02 | 01276 | [16, 20, 24, 36, 51, 54] |
| 2025-11-29 | 01275 | [4, 20, 24, 27, 40, 48]  |
| 2025-11-27 | 01274 | [4, 5, 10, 11, 28, 35]   |
| 2025-11-25 | 01273 | [23, 31, 32, 42, 46, 48] |
| 2025-11-22 | 01272 | [8, 10, 19, 29, 34, 46]  |
| 2025-11-20 | 01271 | [3, 12, 19, 20, 31, 42]  |
| 2025-11-18 | 01270 | [7, 12, 18, 22, 30, 49]  |
| 2025-11-15 | 01269 | [2, 30, 33, 35, 42, 54]  |
| 2025-11-13 | 01268 | [1, 15, 30, 38, 40, 43]  |
| 2025-11-11 | 01267 | [11, 20, 28, 41, 47, 54] |
| 2025-11-08 | 01266 | [14, 16, 19, 22, 27, 44] |
| 2025-11-06 | 01265 | [16, 20, 29, 33, 36, 49] |
| 2025-11-04 | 01264 | [15, 27, 29, 31, 36, 43] |
| 2025-11-01 | 01263 | [7, 11, 28, 29, 31, 33]  |
| 2025-10-30 | 01262 | [20, 23, 35, 41, 47, 55] |
| 2025-10-28 | 01261 | [6, 8, 10, 22, 25, 54]   |
| 2025-10-25 | 01260 | [3, 5, 11, 13, 24, 27]   |
| 2025-10-23 | 01259 | [8, 10, 21, 48, 49, 50]  |

### random 10 tickets of power 6/45

strategy 1:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [1, 13, 14, 21, 27, 43]  |
|   2 | [10, 12, 14, 16, 21, 39] |

strategy 2:
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [5, 7, 24, 34, 36, 39]  |
|   2 | [4, 7, 17, 36, 40, 42]  |
|   3 | [4, 20, 24, 27, 30, 35] |
|   4 | [4, 13, 18, 28, 37, 43] |
|   5 | [6, 9, 30, 34, 40, 44]  |
|   6 | [4, 10, 30, 36, 39, 43] |
|   7 | [4, 11, 16, 22, 33, 44] |
|   8 | [5, 20, 26, 29, 39, 43] |
|   9 | [9, 16, 23, 37, 42, 44] |
|  10 | [9, 23, 29, 37, 41, 44] |

## top 20 details power 6/45
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2025-12-05 | 01441 | [2, 19, 23, 37, 42, 43]  |
| 2025-12-03 | 01440 | [8, 15, 20, 23, 31, 34]  |
| 2025-11-30 | 01439 | [7, 13, 26, 30, 34, 42]  |
| 2025-11-28 | 01438 | [2, 9, 17, 23, 39, 41]   |
| 2025-11-26 | 01437 | [2, 8, 15, 19, 30, 38]   |
| 2025-11-23 | 01436 | [4, 12, 19, 42, 43, 44]  |
| 2025-11-21 | 01435 | [8, 11, 18, 25, 28, 35]  |
| 2025-11-19 | 01434 | [9, 12, 19, 30, 40, 43]  |
| 2025-11-16 | 01433 | [15, 20, 31, 33, 34, 45] |
| 2025-11-14 | 01432 | [3, 10, 15, 27, 41, 42]  |
| 2025-11-12 | 01431 | [16, 24, 29, 37, 40, 44] |
| 2025-11-09 | 01430 | [13, 23, 27, 30, 37, 43] |
| 2025-11-07 | 01429 | [3, 4, 20, 28, 39, 42]   |
| 2025-11-05 | 01428 | [2, 9, 18, 25, 30, 31]   |
| 2025-11-02 | 01427 | [3, 7, 12, 20, 30, 44]   |
| 2025-10-31 | 01426 | [3, 10, 31, 34, 36, 43]  |
| 2025-10-29 | 01425 | [7, 26, 35, 39, 41, 42]  |
| 2025-10-26 | 01424 | [18, 30, 34, 42, 43, 45] |
| 2025-10-24 | 01423 | [2, 11, 24, 31, 32, 38]  |
| 2025-10-22 | 01422 | [5, 11, 12, 24, 28, 44]  |

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

