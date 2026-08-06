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
|   1 | [1, 23, 29, 32, 41, 47]  |
|   2 | [15, 18, 24, 25, 29, 40] |
|   3 | [3, 11, 24, 35, 37, 55]  |
|   4 | [14, 27, 29, 39, 43, 44] |
|   5 | [2, 10, 25, 26, 48, 51]  |
|   6 | [10, 15, 24, 27, 32, 44] |
|   7 | [3, 5, 13, 19, 25, 53]   |
|   8 | [13, 20, 35, 42, 44, 51] |
|   9 | [4, 9, 15, 25, 42, 48]   |
|  10 | [21, 39, 44, 45, 46, 49] |

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
|   1 | [6, 23, 29, 33, 38, 43]  |
|   2 | [8, 19, 26, 34, 45, 52]  |
|   3 | [3, 7, 13, 36, 39, 44]   |
|   4 | [6, 16, 23, 33, 37, 42]  |
|   5 | [11, 24, 31, 35, 41, 49] |
|   6 | [3, 9, 14, 26, 42, 51]   |
|   7 | [2, 4, 8, 16, 34, 38]    |
|   8 | [2, 5, 10, 21, 27, 36]   |
|   9 | [4, 10, 25, 29, 39, 44]  |
|  10 | [5, 27, 36, 39, 42, 47]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [12, 21, 33, 38, 39, 44] |
|   2 | [7, 16, 18, 36, 39, 42]  |
|   3 | [20, 23, 24, 34, 35, 48] |
|   4 | [3, 19, 21, 31, 42, 55]  |
|   5 | [3, 17, 22, 30, 36, 51]  |
|   6 | [9, 12, 13, 20, 39, 47]  |
|   7 | [10, 29, 31, 43, 44, 49] |
|   8 | [19, 22, 23, 29, 40, 43] |
|   9 | [1, 7, 9, 38, 44, 47]    |
|  10 | [3, 11, 16, 32, 33, 37]  |

### latest 20 results
| date       |    id | result                       |
|:-----------|------:|:-----------------------------|
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
| 2026-06-25 | 01363 | [1, 3, 8, 15, 35, 55, 23]    |
| 2026-06-23 | 01362 | [1, 13, 28, 38, 40, 46, 5]   |

## Power 6/45

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [20, 27, 28, 30, 35, 36] |
|   2 | [11, 13, 18, 22, 28, 31] |
|   3 | [18, 24, 26, 40, 42, 45] |
|   4 | [5, 15, 21, 23, 31, 35]  |
|   5 | [7, 9, 19, 25, 31, 33]   |
|   6 | [2, 12, 31, 40, 41, 44]  |
|   7 | [5, 7, 20, 24, 36, 40]   |
|   8 | [12, 16, 20, 22, 29, 30] |
|   9 | [5, 20, 22, 27, 30, 37]  |
|  10 | [4, 24, 33, 37, 40, 43]  |

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
|   1 | [3, 9, 12, 15, 40, 44]   |
|   2 | [2, 5, 9, 28, 32, 36]    |
|   3 | [14, 18, 23, 29, 35, 38] |
|   4 | [3, 13, 18, 27, 41, 43]  |
|   5 | [2, 5, 12, 27, 41, 44]   |
|   6 | [5, 7, 11, 26, 33, 37]   |
|   7 | [5, 18, 23, 28, 31, 43]  |
|   8 | [5, 8, 11, 16, 22, 29]   |
|   9 | [3, 11, 24, 28, 32, 42]  |
|  10 | [4, 25, 27, 30, 38, 42]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 11, 21, 22, 34, 44]  |
|   2 | [1, 2, 13, 35, 37, 42]   |
|   3 | [7, 9, 10, 24, 37, 41]   |
|   4 | [2, 14, 15, 32, 40, 43]  |
|   5 | [16, 17, 24, 34, 35, 38] |
|   6 | [4, 9, 17, 18, 22, 39]   |
|   7 | [4, 11, 15, 16, 38, 40]  |
|   8 | [10, 11, 12, 16, 23, 37] |
|   9 | [10, 15, 20, 23, 34, 43] |
|  10 | [14, 16, 26, 34, 35, 37] |

### latest 20 results
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
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
| 2026-06-24 | 01527 | [3, 11, 17, 19, 30, 32]  |
| 2026-06-21 | 01526 | [3, 8, 19, 27, 41, 45]   |

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

