# Vietlott architecture

Vietlott crawls lottery results from vietlott.vn, stores them as JSON lines, and generates sample
prediction tickets. Everything is a small, dependency-light Python package under `src/`, wired together
by one linear data flow.

## data flow

```text
cli/crawl.py  ─┐
               ├─▶ crawler/products/*  ──▶  data/<product>.jsonl
cli/missing.py ┘     (fetch + parse pages)          │
                                                    ▼
                                    datasource.load_product()   ← single load entry point
                                                    │
                                                    ▼
                                  model/strategy/*  (BaseStrategy subclasses)
                                                    │
                                                    ▼
                                    render_readme.py  ──▶  readme.md
```

1. **crawl** — fetch result pages and append draws to `data/<product>.jsonl`.
2. **backfill** — detect missing draw ids and re-crawl them.
3. **load** — read data through the `datasource` adapter (source-agnostic).
4. **predict** — strategies turn history into tickets.
5. **render** — `render_readme.py` writes the tables you see in `readme.md`.

Every draw is one row with the shared schema `date`, `id`, `result` (`list[int]`; main numbers first,
bonus number last for 6/55).

## project layout

```text
src/vietlott/
  cli/              command-line entry points (crawl, missing)
  config/           product definitions (ProductConfig, get_config)
  crawler/          fetching & parsing draw pages
    products/       one class per product (base, power655, power645, keno)
    requests_helper/  http config + fetch utilities (cookies, threading)
    schema/         attrs request models
    collections_helper.py  small itertools helpers
  datasource.py     single data-loading entry point (jsonl / xlsx)
  model/strategy/   prediction strategies (BaseStrategy + subclasses)
  tests/            test_crawler / test_model / test_data
src/render_readme.py  builds readme.md from data + strategies
data/*.jsonl        crawled draw history
```

## 1. crawling & storing

Products are defined **config-first**, so adding one is mostly data. `config/products.py` holds a
`ProductConfig` per product (`power_655`, `power_645`, `keno`) with its url path, number range, page
size, and threading; `get_config(name)` looks one up.

Results on vietlott.vn are paginated, so fetching is built around page indexes:

- `crawler/products/base.py` `BaseProduct` — shared init (loads `ProductConfig`, headers, optional
  cookies) and the `crawl(run_date_str, index_from, index_to)` / `process_result(...)` contract.
- `crawler/products/{power655,power645,keno}.py` — one subclass per product: `name`, `url`, request
  body, and how to parse a page into rows.
- `crawler/requests_helper/config.py` — default headers and `TIMEOUT`.
- `crawler/requests_helper/fetch.py` — `fetch_wrapper(...)` runs paginated requests (threaded);
  `get_vietlott_cookie()` scrapes the anti-bot cookie when a product needs it (disabled for all
  current products).
- `crawler/schema/requests.py` — `attrs` models for request bodies (e.g. `RequestPower655`).
- `crawler/collections_helper.py` — `chunks_iter` batches page indexes.

The two CLIs drive it:

- `cli/crawl.py` maps a product name to its `BaseProduct` subclass and calls `crawl(...)`.
- `cli/missing.py` compares consecutive draw `id`s, finds gaps, and re-crawls the missing pages.

## 2. loading (datasource adapter)

`vietlott.datasource` is the single place that knows how to read raw data, so strategies never care
about the file format:

- `load_data(path)` dispatches on extension — `.jsonl`/`.json` → jsonl, `.xlsx`/`.xls` → excel.
- `load_product(name)` loads a configured product by its `raw_path`.
- excel without a `result` column is auto-assembled from the number columns.

To support a new source, add a loader to `_LOADERS`; every consumer benefits without changes.

## 3. predicting (strategies)

All strategies live in `model/strategy/` and subclass `BaseStrategy` (`base.py`), which provides the
shared `predict` / `generate` / `backtest` / `evaluate` / `revenue` machinery. They are named by
**method, not library** (e.g. `RandomForestStrategy`, not `SklearnStrategy`).

| strategy | file | uses history? | idea |
|----------|------|---------------|------|
| `RandomStrategy` | `random.py` | no | uniform baseline for comparison |
| `NotRepeatStrategy` | `not_repeat.py` | yes | avoid numbers from the most recent draws |
| `FrequencyStrategy` | `frequency.py` | yes (all past) | Laplace-smoothed frequency + distribution shaping; also exposes `number_probabilities()` and a chi-square `uniformity_test()` |
| `RandomForestStrategy` | `random_forest.py` | yes | RandomForestRegressor over past draws (optional `ml` extra) |
| `LSTMStrategy` | `lstm.py` | yes | LSTM sequence model (optional `ml` extra) |

> **Honest note** (kept in every docstring): lottery draws are independent and uniform, so no strategy
> beats the random baseline in expectation. The value here is clean, measurable, backtestable code — not
> a higher hit rate.

**Key `BaseStrategy` methods**

- `predict(date)` → one ticket; `generate(date, n)` → `n` tickets. Both are causal: only draws before
  `date` are used.
- `backtest()` replays predictions over history, `evaluate()` summarizes hits, and `revenue()` returns
  `(cost, gain, profit)` so any claim is measurable.

**Adding a strategy**

1. create `model/strategy/<name>.py` with `class <Name>Strategy(BaseStrategy)`.
2. implement `predict(self, date=None) -> list[int]` (or override `generate` for batch efficiency).
3. add a test in `tests/test_model/test_strategy.py`.
4. optionally wire it into `render_readme.py`.

## 4. rendering the README

`src/render_readme.py` loads both products, runs the strategies, and writes `readme.md`. It is the
**source of truth for readme.md** — edit the template there, not the generated file. Strategies that need
optional deps degrade gracefully: a note is shown instead of a table when the `ml` extra is missing.

## running

A GitHub Actions workflow crawls daily and pushes back to the repo, so no server is needed. Locally the
installed CLIs are the intended entry points:

```toml
[project.scripts]
vietlott-crawl = "vietlott.cli.crawl:crawl"
vietlott-missing = "vietlott.cli.missing:detect_missing_data"
```

(equivalently `PYTHONPATH=src python src/vietlott/cli/crawl.py <product>`).

## optional dependencies

Heavy deps are gated behind extras in `pyproject.toml` and imported lazily, so the core stays light:

- `ml` (`scikit-learn`, `tensorflow`) — only for `RandomForestStrategy` / `LSTMStrategy`.
- `xls` (`openpyxl`) — only to read excel data.

## tests

```shell
PYTHONPATH=src pytest src/vietlott/tests
```

- `tests/test_crawler` — fetching / schema.
- `tests/test_model` — strategies + backtest/evaluate/revenue.
- `tests/test_data` — the datasource adapter.

Tests needing optional deps use `pytest.importorskip(...)` so they skip cleanly when the extra is absent.