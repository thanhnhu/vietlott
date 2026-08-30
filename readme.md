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
|   1 | [2, 21, 24, 48, 49, 50]  |
|   2 | [2, 9, 32, 44, 45, 50]   |
|   3 | [2, 14, 19, 32, 46, 52]  |
|   4 | [7, 15, 17, 20, 36, 37]  |
|   5 | [22, 45, 46, 48, 49, 55] |
|   6 | [2, 24, 29, 36, 39, 51]  |
|   7 | [8, 16, 32, 34, 36, 42]  |
|   8 | [1, 7, 28, 29, 47, 50]   |
|   9 | [1, 8, 13, 22, 36, 38]   |
|  10 | [1, 7, 21, 31, 39, 54]   |

**strategy 2 - LSTM (Long Short-Term Memory neural network)**
| Tickets                                                       |
|:--------------------------------------------------------------|
| (requires optional 'ml' extra: pip install vietlott-data[ml]) |

**strategy 3 - random forest**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [20, 24, 29, 36, 42, 51] |
|   2 | [2, 6, 39, 44, 48, 52]   |
|   3 | [3, 5, 8, 17, 37, 52]    |
|   4 | [4, 13, 19, 27, 29, 34]  |
|   5 | [8, 22, 27, 34, 45, 52]  |
|   6 | [4, 19, 32, 43, 48, 53]  |
|   7 | [12, 22, 29, 34, 49, 53] |
|   8 | [2, 6, 9, 13, 18, 25]    |
|   9 | [4, 10, 30, 34, 38, 50]  |
|  10 | [3, 6, 8, 10, 12, 49]    |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [4, 12, 13, 24, 26, 43]  |
|   2 | [4, 9, 29, 42, 44, 47]   |
|   3 | [12, 20, 35, 45, 47, 53] |
|   4 | [1, 21, 26, 29, 39, 46]  |
|   5 | [3, 13, 17, 46, 50, 53]  |
|   6 | [11, 17, 23, 36, 38, 54] |
|   7 | [3, 11, 26, 29, 36, 40]  |
|   8 | [3, 9, 43, 44, 51, 53]   |
|   9 | [7, 8, 11, 28, 31, 41]   |
|  10 | [2, 3, 15, 25, 39, 53]   |

**strategy 5 - positional (per-number order statistics), 3 tickets per model**

_frequency:_
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [1, 20, 26, 34, 45, 46]  |
|   2 | [10, 18, 30, 38, 40, 51] |
|   3 | [5, 30, 31, 35, 45, 52]  |

_random forest:_
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [6, 24, 28, 36, 47, 50]  |
|   2 | [13, 23, 44, 50, 51, 54] |
|   3 | [12, 25, 29, 44, 50, 51] |

_LSTM:_
| Tickets                                                       |
|:--------------------------------------------------------------|
| (requires optional 'ml' extra: pip install vietlott-data[ml]) |

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
|   1 | [5, 7, 18, 19, 27, 45]   |
|   2 | [2, 6, 11, 26, 31, 40]   |
|   3 | [5, 17, 18, 21, 29, 45]  |
|   4 | [15, 20, 23, 24, 27, 32] |
|   5 | [5, 13, 14, 15, 19, 31]  |
|   6 | [24, 25, 31, 34, 38, 39] |
|   7 | [2, 9, 13, 23, 40, 43]   |
|   8 | [8, 11, 14, 31, 41, 44]  |
|   9 | [3, 6, 9, 18, 27, 41]    |
|  10 | [4, 32, 33, 35, 37, 45]  |

**strategy 2 - LSTM (Long Short-Term Memory neural network)**
| Tickets                                                       |
|:--------------------------------------------------------------|
| (requires optional 'ml' extra: pip install vietlott-data[ml]) |

**strategy 3 - random forest**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [9, 13, 18, 22, 26, 36]  |
|   2 | [5, 10, 17, 22, 32, 39]  |
|   3 | [17, 21, 25, 28, 31, 43] |
|   4 | [4, 7, 11, 14, 18, 42]   |
|   5 | [2, 5, 9, 17, 23, 28]    |
|   6 | [25, 28, 34, 38, 42, 44] |
|   7 | [4, 13, 18, 28, 38, 42]  |
|   8 | [5, 8, 16, 25, 29, 35]   |
|   9 | [3, 7, 17, 33, 38, 42]   |
|  10 | [6, 14, 18, 25, 41, 43]  |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [6, 11, 12, 18, 27, 31]  |
|   2 | [5, 7, 18, 24, 37, 44]   |
|   3 | [6, 12, 15, 25, 43, 44]  |
|   4 | [5, 14, 19, 23, 30, 38]  |
|   5 | [13, 22, 28, 31, 39, 40] |
|   6 | [5, 9, 21, 22, 27, 41]   |
|   7 | [9, 11, 14, 18, 21, 45]  |
|   8 | [3, 10, 15, 21, 29, 43]  |
|   9 | [12, 13, 23, 34, 36, 43] |
|  10 | [8, 17, 21, 38, 42, 45]  |

**strategy 5 - positional (per-number order statistics), 3 tickets per model**

_frequency:_
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [8, 25, 34, 37, 39, 45] |
|   2 | [4, 13, 34, 41, 43, 45] |
|   3 | [1, 25, 35, 40, 41, 45] |

_random forest:_
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [10, 11, 34, 35, 39, 40] |
|   2 | [6, 19, 35, 37, 39, 40]  |
|   3 | [12, 16, 36, 39, 41, 45] |

_LSTM:_
| Tickets                                                       |
|:--------------------------------------------------------------|
| (requires optional 'ml' extra: pip install vietlott-data[ml]) |

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

