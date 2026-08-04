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
|   1 | [12, 13, 28, 32, 43, 52] |
|   2 | [5, 6, 20, 26, 36, 51]   |
|   3 | [3, 16, 29, 33, 46, 47]  |
|   4 | [1, 7, 9, 13, 18, 34]    |
|   5 | [4, 11, 14, 20, 35, 47]  |
|   6 | [17, 23, 27, 46, 52, 55] |
|   7 | [7, 11, 18, 28, 36, 52]  |
|   8 | [6, 19, 26, 43, 46, 47]  |
|   9 | [12, 22, 26, 33, 41, 42] |
|  10 | [8, 13, 14, 33, 54, 55]  |

**strategy 2 - LSTM (Long Short-Term Memory neural network)**
| Tickets                                                       |
|:--------------------------------------------------------------|
| (requires optional 'ml' extra: pip install vietlott-data[ml]) |

**strategy 3 - random forest**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [10, 18, 28, 31, 37, 50] |
|   2 | [5, 28, 32, 42, 49, 54]  |
|   3 | [3, 7, 9, 16, 19, 26]    |
|   4 | [11, 17, 33, 37, 41, 47] |
|   5 | [3, 8, 22, 39, 51, 54]   |
|   6 | [19, 35, 40, 43, 47, 51] |
|   7 | [11, 17, 26, 30, 48, 52] |
|   8 | [9, 15, 20, 25, 33, 37]  |
|   9 | [5, 11, 17, 24, 30, 41]  |
|  10 | [5, 9, 12, 16, 26, 43]   |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [7, 15, 20, 27, 34, 44]  |
|   2 | [1, 3, 11, 22, 40, 55]   |
|   3 | [5, 13, 16, 29, 31, 37]  |
|   4 | [3, 15, 16, 24, 44, 54]  |
|   5 | [1, 2, 3, 42, 48, 49]    |
|   6 | [1, 6, 21, 24, 45, 54]   |
|   7 | [7, 15, 30, 32, 38, 55]  |
|   8 | [11, 18, 22, 24, 27, 53] |
|   9 | [6, 8, 15, 23, 43, 45]   |
|  10 | [13, 25, 28, 42, 51, 52] |

### latest 20 results
| date       |    id | result                       |
|:-----------|------:|:-----------------------------|
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
| 2026-06-18 | 01360 | [1, 4, 14, 20, 46, 49, 36]   |

## Power 6/45

### predicted tickets

**strategy 1 - random baseline**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [9, 15, 27, 28, 35, 40]  |
|   2 | [4, 15, 17, 27, 37, 45]  |
|   3 | [11, 15, 19, 25, 31, 41] |
|   4 | [4, 13, 16, 31, 32, 35]  |
|   5 | [1, 5, 11, 22, 35, 36]   |
|   6 | [2, 10, 12, 24, 27, 30]  |
|   7 | [9, 12, 17, 20, 29, 35]  |
|   8 | [7, 9, 19, 28, 33, 38]   |
|   9 | [4, 5, 21, 23, 24, 43]   |
|  10 | [2, 8, 14, 23, 35, 37]   |

**strategy 2 - LSTM (Long Short-Term Memory neural network)**
| Tickets                                                       |
|:--------------------------------------------------------------|
| (requires optional 'ml' extra: pip install vietlott-data[ml]) |

**strategy 3 - random forest**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [5, 9, 12, 18, 40, 43]   |
|   2 | [3, 9, 14, 18, 31, 37]   |
|   3 | [5, 9, 14, 20, 32, 42]   |
|   4 | [8, 12, 24, 29, 34, 41]  |
|   5 | [11, 15, 22, 26, 40, 44] |
|   6 | [5, 10, 13, 16, 20, 37]  |
|   7 | [4, 6, 25, 28, 35, 38]   |
|   8 | [20, 28, 33, 38, 42, 44] |
|   9 | [4, 8, 15, 20, 36, 40]   |
|  10 | [5, 9, 13, 16, 20, 43]   |

**strategy 4 - frequency-weighted**
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [5, 7, 20, 24, 39, 41]   |
|   2 | [2, 3, 18, 23, 27, 38]   |
|   3 | [7, 16, 18, 30, 31, 45]  |
|   4 | [10, 11, 12, 28, 32, 43] |
|   5 | [2, 24, 30, 31, 35, 36]  |
|   6 | [2, 7, 11, 23, 34, 36]   |
|   7 | [8, 9, 20, 23, 28, 34]   |
|   8 | [1, 24, 26, 33, 38, 45]  |
|   9 | [19, 25, 26, 27, 31, 33] |
|  10 | [9, 20, 26, 35, 37, 38]  |

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

