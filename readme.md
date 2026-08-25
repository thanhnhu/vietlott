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
|   1 | [3, 16, 24, 45, 49, 50]  |
|   2 | [1, 10, 14, 27, 28, 52]  |
|   3 | [10, 16, 30, 42, 44, 52] |
|   4 | [24, 26, 32, 38, 40, 45] |
|   5 | [5, 9, 15, 28, 35, 41]   |
|   6 | [10, 30, 37, 42, 45, 55] |
|   7 | [9, 28, 37, 44, 47, 48]  |
|   8 | [4, 21, 31, 34, 36, 51]  |
|   9 | [14, 19, 21, 31, 32, 42] |
|  10 | [4, 11, 27, 34, 51, 54]  |

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
|   1 | [17, 22, 28, 32, 39, 51] |
|   2 | [8, 11, 15, 20, 48, 53]  |
|   3 | [17, 27, 32, 36, 49, 52] |
|   4 | [3, 11, 23, 27, 36, 41]  |
|   5 | [3, 6, 10, 21, 29, 35]   |
|   6 | [10, 24, 28, 31, 36, 49] |
|   7 | [5, 11, 16, 21, 47, 52]  |
|   8 | [11, 21, 26, 36, 50, 53] |
|   9 | [7, 14, 17, 26, 45, 52]  |
|  10 | [3, 9, 20, 35, 42, 51]   |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 16, 22, 29, 30, 41]  |
|   2 | [11, 17, 28, 42, 43, 51] |
|   3 | [5, 9, 23, 36, 43, 54]   |
|   4 | [7, 19, 25, 29, 34, 50]  |
|   5 | [2, 33, 34, 39, 40, 44]  |
|   6 | [6, 21, 23, 25, 34, 51]  |
|   7 | [4, 7, 11, 22, 25, 54]   |
|   8 | [1, 10, 25, 31, 37, 43]  |
|   9 | [7, 12, 31, 38, 44, 49]  |
|  10 | [8, 11, 17, 25, 29, 35]  |

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
|   1 | [7, 15, 20, 23, 34, 42]  |
|   2 | [3, 5, 21, 36, 38, 43]   |
|   3 | [3, 6, 22, 23, 28, 43]   |
|   4 | [10, 12, 17, 35, 44, 45] |
|   5 | [1, 14, 20, 23, 42, 44]  |
|   6 | [9, 10, 23, 24, 29, 42]  |
|   7 | [2, 26, 28, 36, 38, 42]  |
|   8 | [6, 11, 16, 25, 39, 41]  |
|   9 | [2, 7, 13, 37, 44, 45]   |
|  10 | [9, 13, 22, 23, 25, 30]  |

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
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [4, 11, 19, 29, 32, 41] |
|   2 | [6, 24, 29, 32, 37, 43] |
|   3 | [3, 7, 12, 16, 21, 43]  |
|   4 | [7, 11, 14, 22, 28, 42] |
|   5 | [8, 14, 19, 27, 33, 43] |
|   6 | [3, 6, 9, 29, 33, 38]   |
|   7 | [5, 19, 24, 29, 33, 43] |
|   8 | [4, 15, 19, 26, 30, 36] |
|   9 | [7, 10, 31, 36, 40, 44] |
|  10 | [7, 13, 18, 22, 32, 42] |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [7, 8, 11, 20, 22, 37]   |
|   2 | [2, 5, 22, 31, 33, 39]   |
|   3 | [13, 22, 25, 27, 33, 42] |
|   4 | [4, 11, 13, 19, 40, 45]  |
|   5 | [7, 10, 26, 29, 40, 44]  |
|   6 | [1, 8, 11, 16, 40, 43]   |
|   7 | [8, 13, 16, 30, 38, 39]  |
|   8 | [1, 8, 26, 29, 31, 43]   |
|   9 | [1, 7, 18, 21, 32, 36]   |
|  10 | [11, 14, 16, 29, 32, 35] |

### latest 20 results
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
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
| 2026-07-10 | 01534 | [9, 17, 23, 26, 42, 44]  |

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

