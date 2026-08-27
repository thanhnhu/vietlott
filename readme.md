# Vietlott

auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)

See [ARCHITECTURE.md](ARCHITECTURE.md) for how the project is structured (crawler, data adapter, strategies).

## Predictions

Sample tickets from several strategies. Lottery draws are independent and uniform, so none of these beat
random in the long run - for testing only, not financial advice.

## Power 6/55

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [19, 22, 27, 32, 43, 49] |
|   2 | [1, 3, 5, 7, 39, 43]     |
|   3 | [9, 13, 30, 33, 49, 50]  |
|   4 | [6, 15, 16, 21, 54, 55]  |
|   5 | [11, 15, 16, 33, 42, 55] |
|   6 | [10, 13, 21, 27, 28, 52] |
|   7 | [12, 18, 35, 42, 48, 55] |
|   8 | [12, 23, 25, 40, 46, 51] |
|   9 | [9, 12, 26, 29, 30, 53]  |
|  10 | [13, 15, 17, 18, 37, 45] |

**strategy 2 - LSTM (Long Short-Term Memory neural network)**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [6, 11, 15, 21, 30, 40]  |
|   2 | [6, 11, 20, 22, 26, 28]  |
|   3 | [19, 21, 48, 49, 54, 55] |
|   4 | [3, 6, 7, 8, 9, 49]      |
|   5 | [1, 2, 3, 17, 26, 53]    |
|   6 | [2, 10, 16, 17, 33, 36]  |
|   7 | [3, 5, 13, 40, 41, 45]   |
|   8 | [1, 11, 22, 26, 33, 51]  |
|   9 | [16, 22, 23, 33, 36, 38] |
|  10 | [20, 21, 22, 31, 43, 45] |

**strategy 3 - random forest**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 9, 20, 38, 47, 52]   |
|   2 | [10, 16, 33, 37, 47, 51] |
|   3 | [4, 7, 16, 41, 47, 51]   |
|   4 | [26, 37, 42, 45, 48, 52] |
|   5 | [2, 4, 8, 12, 16, 20]    |
|   6 | [2, 7, 27, 31, 47, 50]   |
|   7 | [15, 19, 28, 34, 41, 50] |
|   8 | [12, 17, 30, 34, 38, 42] |
|   9 | [23, 31, 34, 39, 44, 48] |
|  10 | [11, 16, 21, 26, 44, 47] |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [1, 4, 14, 28, 41, 49]   |
|   2 | [13, 21, 26, 28, 32, 48] |
|   3 | [11, 13, 22, 23, 36, 43] |
|   4 | [5, 24, 31, 33, 41, 52]  |
|   5 | [6, 17, 34, 47, 52, 53]  |
|   6 | [3, 10, 16, 28, 43, 54]  |
|   7 | [12, 18, 22, 35, 38, 47] |
|   8 | [4, 17, 18, 27, 43, 46]  |
|   9 | [7, 16, 24, 25, 48, 50]  |
|  10 | [7, 12, 34, 40, 44, 55]  |

### latest 20 results
| date       |    id | result                       |
|:-----------|------:|:-----------------------------|
| 2026-08-27 | 01390 | [1, 3, 11, 21, 26, 44, 10]   |
| 2026-08-25 | 01389 | [5, 7, 13, 18, 31, 40, 14]   |
| 2026-08-22 | 01388 | [9, 18, 19, 21, 25, 36, 8]   |
| 2026-08-20 | 01387 | [2, 8, 29, 38, 39, 51, 47]   |
| 2026-08-18 | 01386 | [3, 15, 18, 38, 41, 48, 30]  |
| 2026-08-15 | 01385 | [16, 20, 25, 27, 30, 50, 2]  |
| 2026-08-13 | 01384 | [5, 9, 27, 29, 45, 46, 42]   |
| 2026-08-11 | 01383 | [2, 7, 19, 20, 39, 50, 31]   |
| 2026-08-08 | 01382 | [5, 29, 33, 38, 40, 45, 37]  |
| 2026-08-06 | 01381 | [14, 18, 23, 35, 51, 55, 1]  |
| 2026-08-04 | 01380 | [14, 39, 40, 42, 47, 54, 31] |
| 2026-08-01 | 01379 | [11, 14, 16, 44, 49, 55, 39] |
| 2026-07-30 | 01378 | [2, 12, 24, 28, 43, 49, 51]  |
| 2026-07-28 | 01377 | [7, 22, 23, 27, 41, 44, 48]  |
| 2026-07-25 | 01376 | [5, 9, 27, 33, 37, 50, 48]   |
| 2026-07-23 | 01375 | [1, 3, 8, 38, 40, 55, 36]    |
| 2026-07-21 | 01374 | [8, 11, 22, 24, 32, 39, 13]  |
| 2026-07-18 | 01373 | [22, 41, 45, 48, 54, 55, 16] |
| 2026-07-16 | 01372 | [19, 20, 33, 45, 48, 53, 21] |
| 2026-07-14 | 01371 | [10, 24, 30, 35, 45, 51, 33] |

## Power 6/45

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [13, 16, 31, 40, 42, 43] |
|   2 | [2, 4, 31, 36, 43, 45]   |
|   3 | [2, 10, 11, 18, 29, 39]  |
|   4 | [2, 4, 27, 28, 34, 35]   |
|   5 | [6, 28, 30, 32, 34, 44]  |
|   6 | [1, 4, 6, 17, 19, 22]    |
|   7 | [9, 14, 20, 23, 37, 42]  |
|   8 | [7, 12, 28, 41, 42, 44]  |
|   9 | [1, 4, 9, 17, 37, 38]    |
|  10 | [8, 13, 24, 25, 32, 44]  |

**strategy 2 - LSTM (Long Short-Term Memory neural network)**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [7, 8, 10, 24, 33, 44]   |
|   2 | [9, 12, 23, 26, 28, 43]  |
|   3 | [10, 11, 16, 22, 28, 35] |
|   4 | [2, 3, 7, 25, 33, 34]    |
|   5 | [16, 18, 24, 26, 40, 44] |
|   6 | [1, 2, 6, 7, 16, 27]     |
|   7 | [2, 18, 21, 23, 30, 31]  |
|   8 | [19, 21, 30, 31, 37, 43] |
|   9 | [2, 7, 25, 29, 39, 45]   |
|  10 | [5, 20, 22, 25, 28, 32]  |

**strategy 3 - random forest**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [14, 20, 27, 37, 41, 44] |
|   2 | [9, 15, 18, 22, 38, 43]  |
|   3 | [5, 21, 28, 32, 39, 42]  |
|   4 | [9, 17, 24, 27, 31, 42]  |
|   5 | [4, 9, 15, 28, 33, 37]   |
|   6 | [10, 14, 17, 21, 23, 26] |
|   7 | [6, 10, 17, 36, 40, 44]  |
|   8 | [4, 6, 9, 13, 20, 26]    |
|   9 | [2, 5, 8, 11, 19, 43]    |
|  10 | [14, 25, 28, 32, 35, 40] |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 8, 15, 21, 36, 37]   |
|   2 | [4, 6, 24, 27, 31, 38]   |
|   3 | [8, 10, 18, 21, 31, 35]  |
|   4 | [9, 15, 16, 32, 35, 45]  |
|   5 | [22, 23, 27, 32, 34, 39] |
|   6 | [11, 17, 18, 28, 44, 45] |
|   7 | [6, 10, 27, 28, 39, 43]  |
|   8 | [5, 17, 23, 34, 38, 44]  |
|   9 | [7, 18, 22, 39, 43, 45]  |
|  10 | [5, 13, 20, 23, 33, 36]  |

### latest 20 results
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2026-08-26 | 01554 | [3, 10, 11, 16, 33, 40]  |
| 2026-08-23 | 01553 | [4, 16, 17, 22, 32, 39]  |
| 2026-08-21 | 01552 | [7, 26, 31, 38, 43, 45]  |
| 2026-08-19 | 01551 | [6, 15, 18, 33, 40, 43]  |
| 2026-08-16 | 01550 | [6, 7, 15, 19, 36, 41]   |
| 2026-08-14 | 01549 | [7, 9, 13, 31, 35, 44]   |
| 2026-08-12 | 01548 | [15, 17, 22, 29, 33, 40] |
| 2026-08-09 | 01547 | [3, 17, 20, 27, 31, 35]  |
| 2026-08-07 | 01546 | [2, 8, 19, 30, 36, 43]   |
| 2026-08-05 | 01545 | [2, 6, 11, 16, 28, 39]   |
| 2026-08-02 | 01544 | [3, 12, 20, 25, 27, 37]  |
| 2026-07-31 | 01543 | [6, 16, 24, 25, 38, 43]  |
| 2026-07-29 | 01542 | [2, 6, 21, 31, 36, 45]   |
| 2026-07-26 | 01541 | [13, 16, 27, 33, 41, 44] |
| 2026-07-24 | 01540 | [12, 16, 36, 38, 41, 45] |
| 2026-07-22 | 01539 | [3, 32, 33, 34, 39, 43]  |
| 2026-07-19 | 01538 | [12, 22, 24, 26, 31, 37] |
| 2026-07-17 | 01537 | [9, 18, 30, 31, 39, 45]  |
| 2026-07-15 | 01536 | [7, 11, 29, 37, 43, 45]  |
| 2026-07-12 | 01535 | [6, 9, 11, 17, 35, 44]   |

<!---
stats 6/55 all time - stats.to_markdown(index=False)
stats 6/55 -15d - stats_15d.to_markdown(index=False)
stats 6/55 -30d - stats_30d.to_markdown(index=False)
stats 6/55 -60d - stats_60d.to_markdown(index=False)
stats 6/55 -90d - stats_90d.to_markdown(index=False)
-->

## Install

### run locally

```shell
pip install -r requirements.txt
pip install -e .[ml]  # optional: enables RandomForest / LSTM strategies
python src/vietlott/cli/crawl.py power_655
python src/vietlott/cli/missing.py power_655
python src/render_readme.py
python src/vietlott/model/strategy/random_forest.py
python src/vietlott/model/strategy/lstm.py
```

### via pip

```shell
pip install -i https://test.pypi.org/simple/ vietlott-data==0.1.2
```

### cli

project provides two cli

#### crawl

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

#### Backfill missing data

```shell
Usage: vietlott-missing [OPTIONS] PRODUCT

  detect_missing_data and run if needed :param ctx: context :param product:
  product to run :param limit: number of pages to run :return:

Options:
  --limit INTEGER
  --help           Show this message and exit.
```

