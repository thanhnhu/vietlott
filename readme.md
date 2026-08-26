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
|   1 | [10, 20, 37, 40, 50, 55] |
|   2 | [3, 19, 23, 33, 47, 51]  |
|   3 | [9, 22, 28, 37, 43, 45]  |
|   4 | [15, 36, 38, 39, 40, 48] |
|   5 | [8, 19, 42, 46, 48, 54]  |
|   6 | [21, 29, 34, 49, 51, 55] |
|   7 | [6, 10, 11, 12, 43, 50]  |
|   8 | [11, 22, 23, 37, 42, 48] |
|   9 | [11, 31, 32, 37, 39, 41] |
|  10 | [3, 10, 19, 22, 47, 51]  |

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
|   1 | [29, 34, 37, 41, 47, 52] |
|   2 | [14, 18, 31, 37, 48, 53] |
|   3 | [7, 16, 21, 24, 46, 51]  |
|   4 | [10, 17, 23, 31, 44, 49] |
|   5 | [10, 15, 29, 34, 39, 51] |
|   6 | [2, 5, 8, 16, 43, 48]    |
|   7 | [3, 7, 17, 21, 29, 39]   |
|   8 | [9, 13, 22, 36, 47, 52]  |
|   9 | [3, 8, 23, 29, 35, 52]   |
|  10 | [9, 17, 22, 34, 43, 51]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [7, 13, 29, 39, 40, 52]  |
|   2 | [11, 18, 20, 22, 47, 54] |
|   3 | [9, 14, 16, 25, 36, 41]  |
|   4 | [5, 20, 35, 37, 42, 55]  |
|   5 | [5, 10, 15, 30, 38, 52]  |
|   6 | [7, 28, 32, 40, 46, 53]  |
|   7 | [15, 17, 18, 22, 51, 54] |
|   8 | [9, 11, 29, 37, 38, 55]  |
|   9 | [4, 7, 27, 29, 39, 52]   |
|  10 | [16, 23, 28, 33, 38, 41] |

### latest 20 results
| date       |    id | result                       |
|:-----------|------:|:-----------------------------|
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
| 2026-07-11 | 01370 | [9, 17, 20, 33, 41, 42, 40]  |

## Power 6/45

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [11, 26, 34, 38, 39, 40] |
|   2 | [1, 3, 10, 15, 18, 22]   |
|   3 | [1, 20, 27, 33, 40, 42]  |
|   4 | [14, 25, 31, 42, 44, 45] |
|   5 | [12, 14, 21, 24, 26, 29] |
|   6 | [2, 6, 8, 23, 35, 37]    |
|   7 | [9, 12, 13, 36, 41, 43]  |
|   8 | [8, 14, 15, 24, 25, 31]  |
|   9 | [13, 20, 25, 30, 37, 44] |
|  10 | [8, 14, 26, 32, 38, 40]  |

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
|   1 | [10, 19, 25, 34, 39, 43] |
|   2 | [4, 8, 11, 18, 39, 42]   |
|   3 | [3, 12, 18, 24, 29, 40]  |
|   4 | [8, 14, 23, 30, 37, 41]  |
|   5 | [2, 5, 9, 11, 16, 31]    |
|   6 | [6, 8, 13, 21, 25, 43]   |
|   7 | [9, 20, 25, 36, 39, 43]  |
|   8 | [2, 5, 9, 15, 21, 27]    |
|   9 | [6, 8, 13, 35, 40, 43]   |
|  10 | [6, 9, 12, 15, 20, 30]   |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [12, 15, 17, 22, 29, 38] |
|   2 | [5, 8, 10, 31, 36, 42]   |
|   3 | [4, 8, 25, 30, 35, 40]   |
|   4 | [6, 11, 24, 30, 33, 45]  |
|   5 | [9, 10, 12, 25, 28, 44]  |
|   6 | [2, 22, 25, 29, 40, 44]  |
|   7 | [5, 8, 18, 21, 24, 34]   |
|   8 | [13, 16, 24, 32, 41, 44] |
|   9 | [1, 16, 22, 25, 34, 44]  |
|  10 | [11, 16, 17, 29, 36, 37] |

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

