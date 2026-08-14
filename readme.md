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
|   1 | [1, 2, 20, 25, 30, 34]   |
|   2 | [5, 41, 43, 48, 52, 55]  |
|   3 | [11, 15, 37, 41, 44, 47] |
|   4 | [14, 15, 25, 27, 44, 49] |
|   5 | [16, 22, 33, 46, 51, 55] |
|   6 | [5, 8, 15, 31, 37, 39]   |
|   7 | [4, 24, 30, 34, 42, 50]  |
|   8 | [14, 18, 25, 34, 44, 54] |
|   9 | [6, 15, 28, 30, 33, 42]  |
|  10 | [13, 14, 17, 21, 31, 50] |

**strategy 2 - LSTM (Long Short-Term Memory neural network)**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [6, 11, 20, 22, 26, 28]  |
|   2 | [19, 21, 48, 49, 54, 55] |
|   3 | [3, 6, 7, 8, 9, 49]      |
|   4 | [1, 2, 3, 17, 26, 53]    |
|   5 | [2, 10, 16, 17, 33, 36]  |
|   6 | [3, 5, 13, 40, 41, 45]   |
|   7 | [1, 11, 22, 26, 33, 51]  |
|   8 | [16, 22, 23, 33, 36, 38] |
|   9 | [20, 21, 22, 31, 43, 45] |
|  10 | [8, 10, 12, 24, 40, 44]  |

**strategy 3 - random forest**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [5, 15, 18, 24, 37, 52]  |
|   2 | [12, 16, 22, 40, 47, 52] |
|   3 | [5, 14, 18, 22, 27, 42]  |
|   4 | [2, 5, 9, 21, 27, 43]    |
|   5 | [8, 15, 20, 39, 49, 53]  |
|   6 | [10, 26, 44, 48, 51, 54] |
|   7 | [3, 7, 15, 39, 47, 50]   |
|   8 | [8, 18, 40, 46, 49, 52]  |
|   9 | [7, 14, 30, 35, 39, 44]  |
|  10 | [3, 6, 9, 27, 34, 42]    |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 6, 17, 29, 31, 48]   |
|   2 | [10, 22, 34, 45, 47, 49] |
|   3 | [2, 5, 25, 28, 30, 32]   |
|   4 | [11, 20, 24, 47, 51, 53] |
|   5 | [3, 13, 24, 43, 48, 53]  |
|   6 | [3, 5, 24, 25, 26, 40]   |
|   7 | [7, 11, 18, 30, 45, 53]  |
|   8 | [15, 24, 30, 41, 49, 51] |
|   9 | [6, 16, 17, 25, 34, 51]  |
|  10 | [1, 6, 34, 49, 53, 54]   |

### latest 20 results
| date       |    id | result                       |
|:-----------|------:|:-----------------------------|
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
| 2026-07-07 | 01368 | [4, 6, 25, 32, 33, 44, 8]    |
| 2026-07-04 | 01367 | [13, 15, 18, 23, 31, 43, 41] |
| 2026-07-02 | 01366 | [5, 11, 28, 34, 41, 42, 49]  |
| 2026-06-30 | 01365 | [5, 13, 18, 22, 43, 44, 47]  |

## Power 6/45

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 5, 8, 21, 28, 33]    |
|   2 | [16, 17, 19, 29, 30, 31] |
|   3 | [11, 29, 30, 32, 35, 38] |
|   4 | [8, 10, 21, 24, 30, 37]  |
|   5 | [15, 19, 30, 32, 38, 41] |
|   6 | [2, 9, 24, 30, 32, 33]   |
|   7 | [2, 13, 18, 19, 38, 45]  |
|   8 | [1, 9, 22, 36, 42, 45]   |
|   9 | [20, 31, 33, 34, 40, 44] |
|  10 | [7, 11, 14, 32, 39, 40]  |

**strategy 2 - LSTM (Long Short-Term Memory neural network)**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [9, 12, 23, 26, 28, 43]  |
|   2 | [10, 11, 16, 22, 28, 35] |
|   3 | [2, 3, 7, 25, 33, 34]    |
|   4 | [16, 18, 24, 26, 40, 44] |
|   5 | [1, 2, 6, 7, 16, 27]     |
|   6 | [2, 18, 21, 23, 30, 31]  |
|   7 | [19, 21, 30, 31, 37, 43] |
|   8 | [2, 7, 25, 29, 39, 45]   |
|   9 | [5, 20, 22, 25, 28, 32]  |
|  10 | [11, 25, 37, 40, 41, 45] |

**strategy 3 - random forest**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 12, 17, 21, 36, 42]  |
|   2 | [9, 13, 24, 27, 31, 36]  |
|   3 | [2, 5, 9, 12, 15, 43]    |
|   4 | [9, 14, 19, 25, 30, 39]  |
|   5 | [4, 7, 10, 24, 28, 33]   |
|   6 | [4, 8, 11, 14, 25, 42]   |
|   7 | [4, 14, 18, 20, 26, 30]  |
|   8 | [2, 6, 11, 28, 41, 44]   |
|   9 | [17, 20, 23, 30, 33, 38] |
|  10 | [4, 9, 25, 29, 37, 41]   |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [1, 12, 17, 19, 40, 42]  |
|   2 | [2, 8, 23, 32, 33, 35]   |
|   3 | [11, 12, 19, 20, 28, 41] |
|   4 | [8, 11, 22, 33, 42, 43]  |
|   5 | [11, 23, 26, 32, 33, 42] |
|   6 | [1, 4, 9, 15, 32, 45]    |
|   7 | [2, 5, 29, 36, 42, 43]   |
|   8 | [15, 19, 26, 28, 32, 38] |
|   9 | [6, 19, 20, 26, 31, 44]  |
|  10 | [9, 11, 18, 28, 29, 35]  |

### latest 20 results
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
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
| 2026-07-08 | 01533 | [13, 14, 22, 26, 37, 44] |
| 2026-07-05 | 01532 | [1, 5, 13, 29, 32, 35]   |
| 2026-07-03 | 01531 | [6, 20, 21, 28, 30, 39]  |
| 2026-07-01 | 01530 | [20, 24, 25, 29, 40, 44] |

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

