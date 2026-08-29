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
|   1 | [21, 23, 29, 38, 50, 53] |
|   2 | [4, 26, 27, 30, 31, 34]  |
|   3 | [7, 11, 28, 41, 42, 48]  |
|   4 | [5, 8, 16, 38, 45, 54]   |
|   5 | [5, 12, 29, 41, 47, 55]  |
|   6 | [1, 8, 22, 37, 39, 53]   |
|   7 | [5, 10, 11, 12, 20, 45]  |
|   8 | [12, 23, 25, 35, 49, 50] |
|   9 | [3, 12, 18, 37, 45, 50]  |
|  10 | [5, 10, 11, 22, 35, 43]  |

**strategy 2 - LSTM (Long Short-Term Memory neural network)**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [8, 28, 30, 33, 40, 43]  |
|   2 | [6, 11, 15, 21, 30, 40]  |
|   3 | [6, 11, 20, 22, 26, 28]  |
|   4 | [19, 21, 48, 49, 54, 55] |
|   5 | [3, 6, 7, 8, 9, 49]      |
|   6 | [1, 2, 3, 17, 26, 53]    |
|   7 | [2, 10, 16, 17, 33, 36]  |
|   8 | [3, 5, 13, 40, 41, 45]   |
|   9 | [1, 11, 22, 26, 33, 51]  |
|  10 | [16, 22, 23, 33, 36, 38] |

**strategy 3 - random forest**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 7, 29, 33, 38, 43]   |
|   2 | [2, 6, 11, 18, 27, 32]   |
|   3 | [3, 8, 14, 20, 25, 31]   |
|   4 | [3, 7, 10, 15, 25, 48]   |
|   5 | [6, 11, 19, 28, 33, 40]  |
|   6 | [23, 31, 35, 38, 43, 48] |
|   7 | [17, 21, 26, 38, 40, 44] |
|   8 | [5, 12, 17, 21, 37, 52]  |
|   9 | [11, 22, 31, 34, 39, 44] |
|  10 | [13, 19, 22, 28, 49, 52] |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 5, 21, 22, 32, 53]   |
|   2 | [6, 24, 31, 47, 50, 54]  |
|   3 | [13, 20, 23, 30, 34, 52] |
|   4 | [14, 16, 21, 31, 32, 39] |
|   5 | [6, 17, 27, 35, 46, 55]  |
|   6 | [5, 8, 9, 15, 37, 53]    |
|   7 | [12, 24, 29, 45, 50, 53] |
|   8 | [11, 13, 28, 38, 44, 46] |
|   9 | [8, 9, 17, 39, 45, 55]   |
|  10 | [1, 17, 29, 49, 52, 55]  |

### latest 20 results
| date       |    id | result                       |
|:-----------|------:|:-----------------------------|
| 2026-08-29 | 01391 | [5, 10, 15, 29, 34, 45, 24]  |
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

## Power 6/45

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 6, 11, 17, 23, 33]   |
|   2 | [2, 9, 10, 20, 22, 23]   |
|   3 | [3, 20, 34, 35, 36, 37]  |
|   4 | [6, 16, 21, 27, 30, 35]  |
|   5 | [2, 9, 28, 29, 30, 32]   |
|   6 | [1, 9, 13, 20, 21, 42]   |
|   7 | [12, 21, 25, 28, 33, 41] |
|   8 | [3, 12, 31, 32, 35, 36]  |
|   9 | [1, 2, 5, 29, 41, 45]    |
|  10 | [3, 11, 12, 24, 28, 33]  |

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
|   1 | [4, 15, 19, 25, 29, 41]  |
|   2 | [5, 16, 29, 33, 38, 43]  |
|   3 | [22, 30, 34, 37, 41, 43] |
|   4 | [9, 13, 15, 19, 32, 38]  |
|   5 | [4, 9, 15, 22, 26, 43]   |
|   6 | [4, 7, 10, 14, 28, 41]   |
|   7 | [9, 21, 25, 36, 41, 44]  |
|   8 | [17, 21, 24, 28, 32, 39] |
|   9 | [6, 20, 23, 27, 31, 41]  |
|  10 | [10, 14, 17, 20, 25, 31] |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 9, 12, 26, 37, 39]   |
|   2 | [9, 10, 13, 21, 23, 38]  |
|   3 | [7, 10, 11, 14, 28, 34]  |
|   4 | [7, 19, 24, 34, 37, 41]  |
|   5 | [12, 22, 25, 28, 36, 45] |
|   6 | [13, 14, 16, 19, 29, 38] |
|   7 | [2, 6, 11, 13, 38, 45]   |
|   8 | [8, 22, 26, 27, 39, 42]  |
|   9 | [9, 15, 16, 17, 33, 37]  |
|  10 | [2, 17, 23, 27, 31, 34]  |

### latest 20 results
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
| 2026-08-28 | 01555 | [3, 13, 15, 22, 36, 39]  |
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

