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
|   1 | [5, 7, 14, 22, 28, 52]   |
|   2 | [13, 15, 27, 29, 47, 54] |
|   3 | [3, 20, 41, 44, 51, 55]  |
|   4 | [11, 17, 21, 33, 41, 49] |
|   5 | [4, 7, 14, 18, 35, 53]   |
|   6 | [4, 13, 21, 47, 49, 50]  |
|   7 | [6, 13, 25, 31, 38, 45]  |
|   8 | [6, 27, 28, 36, 43, 55]  |
|   9 | [7, 14, 18, 22, 27, 51]  |
|  10 | [8, 21, 44, 45, 46, 52]  |

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
|   1 | [5, 13, 18, 22, 27, 42]  |
|   2 | [12, 19, 32, 39, 43, 47] |
|   3 | [3, 7, 15, 44, 50, 53]   |
|   4 | [3, 9, 17, 26, 42, 51]   |
|   5 | [6, 18, 22, 40, 48, 52]  |
|   6 | [9, 14, 19, 36, 48, 51]  |
|   7 | [3, 15, 26, 30, 38, 46]  |
|   8 | [10, 16, 27, 31, 35, 40] |
|   9 | [11, 16, 25, 29, 35, 40] |
|  10 | [23, 31, 38, 42, 46, 51] |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 12, 17, 35, 44, 50]  |
|   2 | [1, 3, 30, 41, 43, 44]   |
|   3 | [8, 9, 28, 34, 38, 55]   |
|   4 | [18, 20, 27, 36, 42, 45] |
|   5 | [1, 17, 21, 46, 47, 54]  |
|   6 | [13, 20, 28, 30, 31, 55] |
|   7 | [6, 15, 22, 30, 38, 45]  |
|   8 | [9, 17, 31, 43, 44, 47]  |
|   9 | [4, 12, 19, 25, 46, 47]  |
|  10 | [3, 9, 25, 33, 48, 55]   |

### latest 20 results
| date       |    id | result                       |
|:-----------|------:|:-----------------------------|
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
| 2026-07-09 | 01369 | [2, 9, 10, 14, 17, 49, 45]   |

## Power 6/45

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [7, 17, 22, 23, 28, 44]  |
|   2 | [5, 9, 29, 35, 40, 44]   |
|   3 | [1, 19, 21, 32, 36, 40]  |
|   4 | [6, 19, 22, 33, 37, 38]  |
|   5 | [13, 22, 35, 40, 43, 44] |
|   6 | [4, 6, 15, 24, 35, 44]   |
|   7 | [4, 5, 13, 24, 28, 43]   |
|   8 | [6, 10, 12, 18, 32, 34]  |
|   9 | [14, 16, 23, 25, 29, 44] |
|  10 | [13, 17, 19, 23, 37, 42] |

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
|   1 | [2, 7, 13, 27, 40, 44]   |
|   2 | [17, 21, 30, 35, 37, 42] |
|   3 | [6, 19, 31, 35, 40, 44]  |
|   4 | [4, 14, 18, 21, 24, 38]  |
|   5 | [9, 12, 23, 27, 32, 37]  |
|   6 | [3, 8, 17, 27, 33, 36]   |
|   7 | [10, 19, 25, 29, 33, 42] |
|   8 | [4, 9, 18, 23, 27, 43]   |
|   9 | [2, 7, 11, 14, 35, 42]   |
|  10 | [7, 10, 13, 15, 19, 30]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [8, 11, 24, 26, 40, 41]  |
|   2 | [6, 8, 19, 26, 41, 44]   |
|   3 | [4, 21, 28, 31, 36, 44]  |
|   4 | [17, 20, 21, 26, 27, 35] |
|   5 | [5, 10, 25, 28, 38, 42]  |
|   6 | [7, 10, 15, 32, 33, 42]  |
|   7 | [6, 10, 18, 22, 23, 25]  |
|   8 | [11, 14, 18, 24, 36, 43] |
|   9 | [8, 14, 15, 20, 32, 33]  |
|  10 | [2, 9, 12, 18, 19, 44]   |

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

