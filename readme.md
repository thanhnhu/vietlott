# Vietlott

auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)

See [ARCHITECTURE.md](ARCHITECTURE.md) for how the project is structured (crawler, data adapter, strategies).

## Predictions

Sample tickets from several strategies. Lottery draws are independent and uniform, so none of these beat
random in the long run - for testing only, not financial advice.

## Power 6/55

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [9, 11, 16, 36, 38, 55] |
|   2 | [5, 33, 36, 40, 52, 55] |
|   3 | [1, 4, 5, 26, 36, 50]   |
|   4 | [4, 15, 25, 33, 39, 50] |
|   5 | [5, 24, 25, 29, 42, 47] |
|   6 | [9, 12, 29, 30, 35, 42] |
|   7 | [6, 9, 15, 26, 29, 47]  |
|   8 | [3, 4, 5, 22, 35, 36]   |
|   9 | [6, 19, 20, 23, 41, 53] |
|  10 | [6, 23, 28, 32, 38, 53] |

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
|   1 | [3, 7, 15, 20, 41, 46]   |
|   2 | [8, 14, 20, 34, 41, 53]  |
|   3 | [4, 9, 12, 31, 41, 52]   |
|   4 | [11, 26, 32, 38, 43, 51] |
|   5 | [4, 8, 14, 34, 38, 42]   |
|   6 | [12, 20, 25, 29, 33, 38] |
|   7 | [19, 29, 33, 37, 46, 52] |
|   8 | [5, 14, 17, 35, 45, 50]  |
|   9 | [5, 8, 11, 17, 28, 50]   |
|  10 | [3, 9, 15, 30, 48, 53]   |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [2, 5, 14, 37, 40, 43]   |
|   2 | [5, 22, 31, 41, 46, 48]  |
|   3 | [3, 7, 25, 34, 35, 42]   |
|   4 | [10, 13, 36, 41, 43, 44] |
|   5 | [14, 17, 25, 27, 29, 44] |
|   6 | [10, 20, 30, 44, 47, 55] |
|   7 | [3, 11, 20, 26, 33, 52]  |
|   8 | [1, 6, 19, 24, 32, 47]   |
|   9 | [7, 10, 11, 23, 34, 53]  |
|  10 | [15, 18, 23, 26, 45, 52] |

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
|   1 | [3, 6, 9, 15, 18, 27]    |
|   2 | [17, 24, 25, 26, 42, 45] |
|   3 | [6, 7, 16, 24, 29, 45]   |
|   4 | [3, 7, 12, 16, 21, 31]   |
|   5 | [1, 4, 27, 29, 38, 42]   |
|   6 | [3, 8, 10, 22, 36, 45]   |
|   7 | [7, 13, 16, 34, 43, 45]  |
|   8 | [5, 21, 23, 25, 27, 30]  |
|   9 | [1, 9, 13, 20, 29, 44]   |
|  10 | [6, 16, 18, 22, 28, 43]  |

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
|   1 | [4, 14, 22, 25, 30, 42]  |
|   2 | [5, 24, 29, 37, 41, 44]  |
|   3 | [4, 16, 22, 29, 32, 37]  |
|   4 | [6, 9, 16, 26, 34, 42]   |
|   5 | [11, 16, 22, 28, 31, 34] |
|   6 | [3, 6, 9, 11, 30, 39]    |
|   7 | [8, 12, 14, 20, 23, 41]  |
|   8 | [11, 18, 24, 28, 39, 44] |
|   9 | [4, 30, 34, 35, 40, 43]  |
|  10 | [4, 11, 15, 25, 29, 38]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [16, 23, 28, 29, 30, 40] |
|   2 | [3, 4, 5, 20, 35, 42]    |
|   3 | [5, 21, 24, 30, 36, 37]  |
|   4 | [8, 9, 10, 22, 26, 43]   |
|   5 | [1, 5, 10, 18, 30, 42]   |
|   6 | [13, 14, 20, 23, 31, 33] |
|   7 | [2, 5, 11, 28, 30, 37]   |
|   8 | [1, 12, 22, 26, 37, 44]  |
|   9 | [8, 13, 22, 29, 33, 41]  |
|  10 | [11, 13, 14, 15, 33, 45] |

### latest 20 results
| date       |    id | result                   |
|:-----------|------:|:-------------------------|
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
| 2026-06-24 | 01527 | [3, 11, 17, 19, 30, 32]  |

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

