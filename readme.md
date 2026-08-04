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
|   1 | [9, 18, 30, 36, 37, 46]  |
|   2 | [6, 10, 12, 39, 45, 55]  |
|   3 | [24, 27, 30, 35, 41, 53] |
|   4 | [9, 33, 42, 44, 46, 55]  |
|   5 | [15, 29, 39, 40, 48, 50] |
|   6 | [12, 18, 26, 28, 45, 51] |
|   7 | [2, 12, 21, 22, 29, 32]  |
|   8 | [11, 23, 30, 35, 46, 54] |
|   9 | [6, 33, 37, 44, 45, 50]  |
|  10 | [5, 6, 7, 8, 12, 28]     |

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
|   1 | [17, 21, 42, 46, 51, 53] |
|   2 | [5, 13, 28, 47, 50, 54]  |
|   3 | [17, 22, 40, 44, 48, 53] |
|   4 | [23, 35, 40, 44, 48, 53] |
|   5 | [6, 9, 32, 37, 39, 52]   |
|   6 | [12, 25, 35, 42, 47, 51] |
|   7 | [4, 20, 26, 29, 41, 46]  |
|   8 | [10, 17, 22, 35, 47, 52] |
|   9 | [5, 11, 14, 26, 42, 45]  |
|  10 | [6, 10, 28, 31, 35, 50]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [7, 10, 26, 35, 47, 52]  |
|   2 | [14, 20, 26, 30, 41, 51] |
|   3 | [13, 14, 16, 23, 27, 51] |
|   4 | [1, 14, 16, 22, 37, 47]  |
|   5 | [10, 24, 29, 35, 41, 55] |
|   6 | [3, 15, 17, 21, 36, 40]  |
|   7 | [2, 6, 9, 42, 44, 51]    |
|   8 | [21, 25, 26, 32, 42, 52] |
|   9 | [10, 24, 38, 39, 41, 42] |
|  10 | [1, 14, 27, 48, 50, 54]  |

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
|   1 | [5, 13, 23, 32, 37, 38]  |
|   2 | [2, 6, 18, 22, 26, 38]   |
|   3 | [8, 9, 13, 25, 27, 29]   |
|   4 | [10, 15, 21, 23, 35, 37] |
|   5 | [8, 14, 17, 26, 32, 36]  |
|   6 | [2, 4, 10, 28, 38, 41]   |
|   7 | [12, 28, 30, 31, 34, 42] |
|   8 | [17, 23, 31, 39, 41, 42] |
|   9 | [3, 4, 7, 15, 17, 39]    |
|  10 | [7, 21, 29, 31, 32, 42]  |

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
|   1 | [2, 5, 8, 23, 26, 40]    |
|   2 | [6, 22, 26, 36, 40, 43]  |
|   3 | [1, 4, 8, 12, 25, 31]    |
|   4 | [3, 8, 32, 35, 38, 43]   |
|   5 | [3, 7, 10, 13, 24, 38]   |
|   6 | [3, 12, 25, 29, 32, 35]  |
|   7 | [4, 9, 13, 16, 27, 32]   |
|   8 | [25, 29, 33, 37, 41, 44] |
|   9 | [7, 11, 15, 30, 34, 41]  |
|  10 | [15, 19, 22, 25, 36, 42] |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 9, 12, 24, 26, 45]   |
|   2 | [4, 12, 17, 25, 33, 40]  |
|   3 | [3, 7, 10, 25, 35, 42]   |
|   4 | [1, 8, 19, 23, 25, 33]   |
|   5 | [10, 12, 14, 37, 40, 45] |
|   6 | [6, 14, 20, 23, 25, 40]  |
|   7 | [5, 11, 14, 24, 27, 30]  |
|   8 | [6, 7, 12, 19, 28, 41]   |
|   9 | [15, 17, 28, 29, 32, 36] |
|  10 | [2, 7, 25, 34, 37, 39]   |

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

