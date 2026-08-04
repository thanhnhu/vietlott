import random

from vietlott.model.strategy.base import BaseStrategy


class NotRepeatStrategy(BaseStrategy):
    """avoid numbers drawn in the most recent ``lookback`` draws, then pick uniformly.

    the "numbers are due / won't repeat" gambler heuristic. it does not beat the
    uniform baseline in expectation, but it is well-defined and backtestable.
    """

    def __init__(self, *args, lookback: int = 1, **kwargs):
        super().__init__(*args, **kwargs)
        self.lookback = lookback

    def predict(self, date=None):
        # collect numbers from the last ``lookback`` draws (assumed "not due to repeat")
        history = self._history_before(date)
        recent = set()
        for draw in history.tail(self.lookback):
            recent.update(draw)

        # draw only from numbers that did NOT appear recently
        pool = [n for n in range(self.min_val, self.max_val + 1) if n not in recent]
        if len(pool) < self.number_predict:  # early history: not enough left, fall back to all
            pool = list(range(self.min_val, self.max_val + 1))

        return sorted(random.sample(pool, self.number_predict))
