# Vietlott

auto crawl lottery data from [vietlott](https://vietlott.vn) daily, and predict tickets - it's a copy from [here](https://github.com/vietvudanh/vietlott-data)

## Predictions (just for testing, not a financial advice)

### random 10 tickets of power 6/55

strategy 1 (random baseline - backtest hits):
| date   | result   | predicted   |
|--------|----------|-------------|

strategy 2 (LSTM - Long Short-Term Memory neural network):
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [19, 21, 48, 49, 54, 55] |
|   2 | [3, 6, 7, 8, 9, 49]      |

strategy 3 (random forest):
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [3, 10, 22, 31, 48, 52]  |
|   2 | [4, 16, 21, 29, 35, 48]  |
|   3 | [4, 9, 29, 33, 40, 51]   |
|   4 | [19, 24, 28, 32, 44, 49] |
|   5 | [5, 11, 17, 21, 24, 27]  |
|   6 | [3, 7, 11, 20, 46, 52]   |
|   7 | [11, 15, 32, 42, 48, 53] |
|   8 | [4, 28, 32, 37, 41, 51]  |
|   9 | [14, 20, 25, 28, 33, 46] |
|  10 | [4, 26, 32, 42, 46, 51]  |

strategy 4 (frequency-weighted):
|   # | Tickets                 |
|----:|:------------------------|
|   1 | [2, 5, 24, 35, 45, 48]  |
|   2 | [7, 15, 37, 40, 42, 44] |
|   3 | [8, 18, 31, 35, 46, 47] |
|   4 | [1, 4, 9, 31, 42, 54]   |
|   5 | [2, 5, 12, 22, 28, 53]  |
|   6 | [2, 3, 22, 33, 50, 54]  |
|   7 | [7, 12, 25, 30, 33, 50] |
|   8 | [5, 11, 27, 30, 39, 42] |
|   9 | [3, 11, 36, 41, 51, 55] |
|  10 | [1, 23, 24, 25, 47, 51] |

## top 20 details power 6/55
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

### random 10 tickets of power 6/45

strategy 1 (LSTM - Long Short-Term Memory neural network):
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [10, 11, 16, 22, 28, 35] |
|   2 | [2, 3, 7, 25, 33, 34]    |

strategy 2 (random forest):
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [27, 32, 35, 40, 42, 44] |
|   2 | [2, 6, 10, 21, 34, 38]   |
|   3 | [3, 6, 16, 22, 31, 37]   |
|   4 | [11, 17, 27, 29, 33, 42] |
|   5 | [2, 4, 8, 12, 19, 40]    |
|   6 | [5, 19, 25, 32, 38, 41]  |
|   7 | [4, 18, 28, 32, 39, 43]  |
|   8 | [3, 9, 13, 28, 40, 44]   |
|   9 | [3, 8, 15, 17, 40, 43]   |
|  10 | [4, 8, 23, 32, 35, 42]   |

strategy 3 (frequency-weighted):
|   # | Tickets                  |
|----:|:-------------------------|
|   1 | [1, 18, 24, 27, 38, 42]  |
|   2 | [12, 15, 20, 25, 43, 44] |
|   3 | [8, 19, 31, 33, 38, 42]  |
|   4 | [2, 16, 19, 33, 43, 44]  |
|   5 | [15, 16, 19, 21, 29, 33] |
|   6 | [8, 11, 19, 20, 29, 32]  |
|   7 | [1, 23, 25, 26, 29, 33]  |
|   8 | [7, 15, 24, 26, 38, 45]  |
|   9 | [10, 14, 19, 24, 29, 39] |
|  10 | [19, 21, 28, 29, 30, 43] |

## top 20 details power 6/45
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

