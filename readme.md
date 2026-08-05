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
|   1 | [25, 27, 31, 33, 41, 49] |
|   2 | [10, 12, 23, 25, 49, 50] |
|   3 | [9, 23, 26, 33, 38, 51]  |
|   4 | [4, 21, 37, 52, 54, 55]  |
|   5 | [15, 26, 28, 37, 46, 53] |
|   6 | [1, 3, 32, 36, 40, 41]   |
|   7 | [5, 7, 27, 40, 49, 55]   |
|   8 | [13, 24, 33, 46, 50, 52] |
|   9 | [2, 3, 19, 24, 33, 38]   |
|  10 | [15, 22, 32, 34, 37, 39] |

**strategy 2 - LSTM (Long Short-Term Memory neural network)**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [19, 21, 48, 49, 54, 55] |
|   2 | [3, 6, 7, 8, 9, 49]      |
|   3 | [1, 2, 3, 17, 26, 53]    |
|   4 | [2, 10, 16, 17, 33, 36]  |
|   5 | [3, 5, 13, 40, 41, 45]   |
|   6 | [1, 11, 22, 26, 33, 51]  |
|   7 | [16, 22, 23, 33, 36, 38] |
|   8 | [20, 21, 22, 31, 43, 45] |
|   9 | [8, 10, 12, 24, 40, 44]  |
|  10 | [7, 8, 15, 24, 26, 48]   |

**strategy 3 - random forest**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [11, 24, 29, 33, 48, 53] |
|   2 | [14, 21, 24, 28, 43, 48] |
|   3 | [15, 19, 29, 36, 39, 51] |
|   4 | [6, 17, 25, 29, 33, 39]  |
|   5 | [3, 6, 11, 19, 25, 33]   |
|   6 | [19, 25, 41, 45, 48, 52] |
|   7 | [4, 15, 32, 36, 47, 50]  |
|   8 | [11, 18, 21, 23, 29, 53] |
|   9 | [6, 18, 38, 43, 48, 51]  |
|  10 | [9, 18, 25, 30, 43, 47]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [14, 18, 22, 33, 34, 37] |
|   2 | [23, 26, 27, 28, 32, 45] |
|   3 | [8, 14, 17, 27, 39, 47]  |
|   4 | [12, 26, 30, 33, 35, 43] |
|   5 | [3, 8, 18, 23, 39, 48]   |
|   6 | [5, 10, 22, 41, 47, 55]  |
|   7 | [1, 4, 29, 30, 34, 49]   |
|   8 | [5, 12, 14, 33, 45, 50]  |
|   9 | [4, 18, 23, 24, 39, 55]  |
|  10 | [8, 12, 14, 48, 49, 51]  |

### latest 20 results
| date       |    id | result                       |
|:-----------|------:|:-----------------------------|
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
| 2026-06-27 | 01364 | [7, 16, 21, 23, 28, 52, 54]  |
| 2026-06-25 | 01363 | [1, 3, 8, 15, 35, 55, 23]    |
| 2026-06-23 | 01362 | [1, 13, 28, 38, 40, 46, 5]   |
| 2026-06-20 | 01361 | [16, 23, 26, 30, 52, 53, 46] |

## Power 6/45

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [1, 23, 28, 37, 44, 45]  |
|   2 | [6, 15, 30, 37, 38, 40]  |
|   3 | [8, 9, 12, 31, 40, 44]   |
|   4 | [21, 22, 26, 27, 29, 37] |
|   5 | [10, 23, 34, 35, 37, 40] |
|   6 | [7, 27, 33, 36, 38, 39]  |
|   7 | [2, 3, 5, 14, 36, 37]    |
|   8 | [2, 6, 9, 15, 36, 40]    |
|   9 | [10, 26, 27, 28, 34, 38] |
|  10 | [8, 11, 16, 21, 23, 34]  |

**strategy 2 - LSTM (Long Short-Term Memory neural network)**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [10, 11, 16, 22, 28, 35] |
|   2 | [2, 3, 7, 25, 33, 34]    |
|   3 | [16, 18, 24, 26, 40, 44] |
|   4 | [1, 2, 6, 7, 16, 27]     |
|   5 | [2, 18, 21, 23, 30, 31]  |
|   6 | [19, 21, 30, 31, 37, 43] |
|   7 | [2, 7, 25, 29, 39, 45]   |
|   8 | [5, 20, 22, 25, 28, 32]  |
|   9 | [11, 25, 37, 40, 41, 45] |
|  10 | [1, 5, 9, 10, 33, 41]    |

**strategy 3 - random forest**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [18, 21, 23, 31, 40, 43] |
|   2 | [4, 12, 16, 20, 32, 36]  |
|   3 | [19, 23, 28, 36, 38, 42] |
|   4 | [5, 13, 17, 27, 33, 43]  |
|   5 | [11, 16, 19, 38, 42, 44] |
|   6 | [22, 26, 30, 33, 37, 41] |
|   7 | [7, 9, 13, 20, 25, 31]   |
|   8 | [3, 6, 18, 29, 33, 38]   |
|   9 | [4, 9, 16, 23, 26, 33]   |
|  10 | [8, 12, 23, 33, 37, 41]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [7, 17, 21, 22, 28, 44]  |
|   2 | [1, 16, 25, 30, 35, 37]  |
|   3 | [5, 6, 17, 20, 23, 34]   |
|   4 | [13, 14, 19, 20, 39, 42] |
|   5 | [2, 3, 15, 24, 29, 45]   |
|   6 | [2, 5, 33, 37, 40, 41]   |
|   7 | [1, 9, 15, 22, 29, 35]   |
|   8 | [4, 10, 27, 34, 39, 44]  |
|   9 | [3, 8, 11, 20, 30, 31]   |
|  10 | [9, 12, 20, 31, 34, 44]  |

### latest 20 results
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
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
| 2026-06-28 | 01529 | [2, 11, 18, 33, 42, 45]  |
| 2026-06-26 | 01528 | [9, 14, 31, 36, 41, 45]  |
| 2026-06-24 | 01527 | [3, 11, 17, 19, 30, 32]  |
| 2026-06-21 | 01526 | [3, 8, 19, 27, 41, 45]   |
| 2026-06-19 | 01525 | [6, 9, 19, 29, 30, 36]   |

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

