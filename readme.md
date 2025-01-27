# Vietlot
auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)
## Predictions (just for testing, not a financial advice)
### random 10 tickets of power 6/55

strategy 1:
| date       | result                   | predicted                |
|:-----------|:-------------------------|:-------------------------|
| 2024-07-16 | [20, 31, 34, 36, 47, 52] | [36, 47, 34, 53, 52, 31] |
| 2018-01-25 | [1, 10, 30, 44, 45, 50]  | [24, 45, 44, 10, 50, 4]  |

strategy 2:
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [4, 14, 31, 42, 47, 49] |

strategy 3:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 10, 31, 35, 39, 52]  |
|   2 | [12, 20, 29, 46, 51, 54] |
|   3 | [8, 24, 29, 35, 39, 49]  |
|   4 | [4, 11, 24, 42, 48, 51]  |
|   5 | [18, 29, 38, 45, 50, 53] |
|   6 | [12, 16, 22, 41, 49, 52] |
|   7 | [5, 30, 35, 39, 48, 53]  |
|   8 | [5, 19, 31, 40, 44, 51]  |
|   9 | [4, 12, 27, 35, 45, 50]  |
|  10 | [5, 14, 22, 35, 40, 51]  |

## top 20 details power 6/55
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2025-01-25 | 01144 | [14, 21, 40, 42, 48, 51] |
| 2025-01-23 | 01143 | [11, 18, 22, 49, 50, 51] |
| 2025-01-21 | 01142 | [11, 18, 22, 28, 51, 52] |
| 2025-01-18 | 01141 | [1, 3, 26, 31, 37, 41]   |
| 2025-01-16 | 01140 | [8, 16, 34, 37, 47, 50]  |
| 2025-01-14 | 01139 | [3, 11, 12, 24, 33, 40]  |
| 2025-01-11 | 01138 | [10, 25, 26, 29, 37, 46] |
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

### random 10 tickets of power 6/45

strategy 1:
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [8, 18, 30, 32, 38, 45] |

strategy 2:
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [6, 11, 24, 29, 40, 44]  |
|   2 | [12, 17, 23, 28, 39, 43] |
|   3 | [11, 27, 35, 39, 40, 43] |
|   4 | [4, 23, 26, 29, 31, 37]  |
|   5 | [3, 12, 25, 29, 33, 36]  |
|   6 | [18, 22, 25, 28, 33, 37] |
|   7 | [4, 7, 25, 32, 40, 43]   |
|   8 | [17, 20, 24, 28, 39, 43] |
|   9 | [3, 22, 27, 37, 40, 43]  |
|  10 | [7, 19, 25, 30, 37, 43]  |

## top 20 details power 6/45
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2025-01-26 | 01308 | [5, 8, 9, 11, 20, 29]    |
| 2025-01-24 | 01307 | [1, 7, 11, 22, 31, 34]   |
| 2025-01-22 | 01306 | [3, 21, 26, 29, 32, 33]  |
| 2025-01-19 | 01305 | [5, 6, 10, 19, 32, 38]   |
| 2025-01-17 | 01304 | [2, 12, 22, 31, 34, 35]  |
| 2025-01-15 | 01303 | [2, 6, 8, 10, 23, 33]    |
| 2025-01-12 | 01302 | [2, 9, 12, 14, 41, 44]   |
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

