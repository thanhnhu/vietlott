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
|   1 | [8, 14, 24, 29, 31, 51]  |
|   2 | [6, 9, 14, 31, 35, 38]   |
|   3 | [15, 29, 40, 43, 44, 45] |
|   4 | [14, 19, 30, 34, 36, 48] |
|   5 | [3, 9, 15, 26, 37, 40]   |
|   6 | [15, 20, 39, 45, 48, 54] |
|   7 | [5, 13, 14, 24, 31, 52]  |
|   8 | [9, 16, 31, 36, 42, 54]  |
|   9 | [1, 11, 15, 41, 53, 55]  |
|  10 | [22, 24, 31, 36, 39, 47] |

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
|   1 | [15, 19, 30, 40, 44, 52] |
|   2 | [5, 8, 12, 18, 27, 47]   |
|   3 | [3, 7, 12, 18, 41, 46]   |
|   4 | [11, 32, 36, 40, 45, 50] |
|   5 | [20, 29, 32, 36, 39, 44] |
|   6 | [3, 14, 23, 27, 45, 49]  |
|   7 | [4, 9, 14, 26, 44, 49]   |
|   8 | [3, 25, 38, 46, 50, 54]  |
|   9 | [5, 10, 20, 29, 39, 48]  |
|  10 | [6, 12, 17, 26, 47, 52]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [16, 18, 21, 29, 48, 52] |
|   2 | [3, 29, 33, 42, 48, 53]  |
|   3 | [13, 15, 25, 26, 31, 47] |
|   4 | [2, 19, 26, 41, 49, 55]  |
|   5 | [8, 17, 30, 32, 37, 54]  |
|   6 | [6, 11, 16, 23, 38, 39]  |
|   7 | [3, 6, 12, 36, 39, 55]   |
|   8 | [10, 14, 33, 39, 42, 44] |
|   9 | [8, 21, 27, 31, 35, 52]  |
|  10 | [5, 6, 9, 21, 35, 55]    |

### latest 20 results
| date       |    id | result                       |
|:-----------|------:|:-----------------------------|
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
| 2026-07-07 | 01368 | [4, 6, 25, 32, 33, 44, 8]    |
| 2026-07-04 | 01367 | [13, 15, 18, 23, 31, 43, 41] |
| 2026-07-02 | 01366 | [5, 11, 28, 34, 41, 42, 49]  |

## Power 6/45

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [15, 22, 26, 32, 33, 41] |
|   2 | [3, 14, 15, 16, 28, 35]  |
|   3 | [4, 11, 23, 37, 40, 42]  |
|   4 | [1, 10, 33, 34, 39, 40]  |
|   5 | [11, 12, 23, 28, 33, 43] |
|   6 | [2, 12, 16, 25, 35, 38]  |
|   7 | [2, 6, 25, 26, 31, 42]   |
|   8 | [7, 18, 19, 41, 44, 45]  |
|   9 | [5, 6, 8, 19, 40, 42]    |
|  10 | [2, 3, 9, 18, 31, 36]    |

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
|   1 | [4, 11, 16, 20, 28, 39]  |
|   2 | [4, 8, 14, 20, 33, 42]   |
|   3 | [4, 11, 15, 30, 34, 39]  |
|   4 | [9, 12, 17, 38, 41, 44]  |
|   5 | [5, 20, 32, 38, 41, 44]  |
|   6 | [2, 6, 8, 11, 16, 30]    |
|   7 | [10, 14, 21, 26, 41, 44] |
|   8 | [6, 19, 23, 31, 35, 43]  |
|   9 | [4, 26, 33, 36, 39, 42]  |
|  10 | [5, 10, 13, 17, 25, 31]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [12, 17, 23, 26, 31, 39] |
|   2 | [3, 5, 27, 37, 39, 44]   |
|   3 | [3, 5, 20, 28, 36, 45]   |
|   4 | [5, 14, 17, 22, 39, 40]  |
|   5 | [5, 17, 21, 25, 35, 42]  |
|   6 | [8, 14, 26, 33, 37, 39]  |
|   7 | [1, 6, 19, 20, 21, 36]   |
|   8 | [3, 16, 25, 33, 34, 37]  |
|   9 | [1, 6, 15, 31, 41, 45]   |
|  10 | [10, 11, 15, 24, 36, 44] |

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

