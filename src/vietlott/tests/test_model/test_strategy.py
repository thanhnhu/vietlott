import pandas as pd
import pytest

from vietlott.model.strategy.base import BaseStrategy
from vietlott.model.strategy.random import RandomStrategy
from vietlott.model.strategy.not_repeat import NotRepeatStrategy
from vietlott.model.strategy.frequency import FrequencyStrategy

MIN_VAL, MAX_VAL, SIZE = 1, 55, 6


@pytest.fixture
def df():
    rows = [
        {"date": "2021-01-01", "id": "00001", "result": [1, 2, 3, 4, 5, 6, 7]},
        {"date": "2021-01-03", "id": "00002", "result": [10, 20, 30, 40, 50, 55, 11]},
        {"date": "2021-01-05", "id": "00003", "result": [2, 8, 19, 33, 41, 52, 9]},
        {"date": "2021-01-07", "id": "00004", "result": [5, 6, 7, 8, 9, 10, 12]},
        {"date": "2021-01-09", "id": "00005", "result": [3, 14, 25, 36, 47, 54, 1]},
    ]
    return pd.DataFrame(rows)


def _assert_valid_ticket(ticket):
    assert len(ticket) == SIZE
    assert len(set(ticket)) == SIZE, "numbers must be distinct"
    assert all(MIN_VAL <= n <= MAX_VAL for n in ticket)
    assert ticket == sorted(ticket)


def test_random_range_and_max_reachable(df):
    model = RandomStrategy(df, min_val=MIN_VAL, max_val=MAX_VAL)
    seen = set()
    for _ in range(300):
        ticket = model.predict()
        _assert_valid_ticket(ticket)
        seen.update(ticket)
    # off-by-one regression: max_val must be reachable
    assert MAX_VAL in seen


def test_not_repeat_excludes_last_draw(df):
    model = NotRepeatStrategy(df, min_val=MIN_VAL, max_val=MAX_VAL, lookback=1)
    last_main = set(df.iloc[-1]["result"][:SIZE])
    for _ in range(50):
        ticket = model.predict("2021-01-11")  # after all draws
        _assert_valid_ticket(ticket)
        assert not (set(ticket) & last_main), "must avoid numbers from the most recent draw"


def test_frequency_valid_and_causal(df):
    model = FrequencyStrategy(df, min_val=MIN_VAL, max_val=MAX_VAL, shape=False)
    for _ in range(50):
        ticket = model.predict("2021-01-11")
        _assert_valid_ticket(ticket)


def test_frequency_no_history_falls_back(df):
    model = FrequencyStrategy(df, min_val=MIN_VAL, max_val=MAX_VAL)
    ticket = model.predict("2020-01-01")  # before any draw -> uniform fallback
    _assert_valid_ticket(ticket)


def test_backtest_evaluate_revenue(df):
    model = RandomStrategy(df, min_val=MIN_VAL, max_val=MAX_VAL, time_predict=2)
    model.backtest()
    result = model.evaluate()
    assert "correct_time" in result
    assert "count_correct_num" in result

    cost, gain, profit = model.revenue()
    assert cost == len(df) * 2 * BaseStrategy.ticket_price
    assert profit == gain - cost
