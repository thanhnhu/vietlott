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
|   1 | [8, 24, 26, 39, 47, 54]  |
|   2 | [2, 29, 32, 39, 45, 47]  |
|   3 | [3, 13, 16, 28, 30, 55]  |
|   4 | [11, 16, 21, 29, 35, 54] |
|   5 | [2, 7, 10, 11, 46, 52]   |
|   6 | [14, 25, 30, 34, 36, 50] |
|   7 | [25, 26, 27, 42, 49, 53] |
|   8 | [22, 28, 31, 35, 46, 50] |
|   9 | [1, 4, 28, 30, 35, 40]   |
|  10 | [4, 9, 23, 42, 50, 52]   |

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
|   1 | [3, 9, 23, 29, 39, 50]   |
|   2 | [4, 10, 27, 31, 38, 49]  |
|   3 | [6, 13, 17, 21, 37, 44]  |
|   4 | [21, 29, 33, 37, 41, 49] |
|   5 | [5, 10, 18, 26, 31, 36]  |
|   6 | [13, 20, 24, 36, 50, 53] |
|   7 | [5, 9, 11, 16, 27, 47]   |
|   8 | [5, 24, 39, 42, 46, 50]  |
|   9 | [4, 13, 19, 27, 31, 41]  |
|  10 | [5, 11, 20, 35, 44, 52]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 20, 25, 35, 45, 49]  |
|   2 | [18, 24, 27, 35, 43, 54] |
|   3 | [13, 21, 26, 27, 34, 44] |
|   4 | [9, 14, 18, 31, 40, 46]  |
|   5 | [6, 16, 26, 41, 43, 45]  |
|   6 | [11, 15, 16, 21, 49, 53] |
|   7 | [21, 25, 36, 42, 43, 49] |
|   8 | [1, 13, 14, 16, 40, 42]  |
|   9 | [3, 11, 16, 19, 30, 49]  |
|  10 | [5, 11, 13, 23, 29, 48]  |

### latest 20 results
| date       |    id | result                       |
|:-----------|------:|:-----------------------------|
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
| 2026-06-27 | 01364 | [7, 16, 21, 23, 28, 52, 54]  |

## Power 6/45

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [2, 11, 13, 15, 16, 18]  |
|   2 | [12, 14, 16, 19, 31, 43] |
|   3 | [3, 14, 15, 27, 31, 34]  |
|   4 | [13, 18, 24, 29, 33, 37] |
|   5 | [1, 11, 14, 16, 36, 37]  |
|   6 | [3, 5, 20, 21, 30, 34]   |
|   7 | [13, 14, 15, 16, 23, 37] |
|   8 | [10, 25, 27, 28, 33, 34] |
|   9 | [1, 7, 28, 29, 41, 43]   |
|  10 | [6, 27, 31, 33, 40, 45]  |

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
|   1 | [4, 14, 31, 36, 40, 43]  |
|   2 | [4, 21, 25, 28, 33, 37]  |
|   3 | [4, 14, 20, 27, 33, 37]  |
|   4 | [2, 7, 13, 16, 21, 25]   |
|   5 | [3, 6, 17, 26, 30, 38]   |
|   6 | [4, 8, 22, 25, 35, 40]   |
|   7 | [25, 30, 33, 36, 38, 42] |
|   8 | [4, 8, 22, 28, 31, 41]   |
|   9 | [2, 6, 16, 21, 24, 38]   |
|  10 | [3, 8, 27, 36, 41, 44]   |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [13, 18, 25, 37, 40, 42] |
|   2 | [3, 8, 21, 29, 35, 43]   |
|   3 | [6, 19, 20, 25, 27, 41]  |
|   4 | [10, 13, 31, 32, 35, 45] |
|   5 | [4, 9, 11, 14, 33, 42]   |
|   6 | [1, 6, 8, 26, 30, 43]    |
|   7 | [9, 16, 17, 28, 34, 35]  |
|   8 | [3, 4, 8, 25, 34, 39]    |
|   9 | [6, 7, 11, 21, 23, 41]   |
|  10 | [5, 8, 22, 40, 42, 43]   |

### latest 20 results
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
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
| 2026-06-28 | 01529 | [2, 11, 18, 33, 42, 45]  |
| 2026-06-26 | 01528 | [9, 14, 31, 36, 41, 45]  |

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

