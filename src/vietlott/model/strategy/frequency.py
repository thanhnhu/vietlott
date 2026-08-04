import random
from collections import Counter

from vietlott.model.strategy.base import BaseStrategy


class FrequencyStrategy(BaseStrategy):
    """frequency-weighted sampling shaped to match historical draw distributions.

    honest note: draws are independent and uniform, so the *expected* return of
    this strategy equals the uniform baseline. its only edge is cosmetic - the
    generated tickets look like real draws (plausible sum and odd/even split),
    which some players prefer. use ``backtest``/``evaluate``/``revenue`` to verify
    it does not actually improve hit rate.

    parameters
    ----------
    lookback: number of most recent draws to weight by (``None`` = all history).
    smoothing: Laplace smoothing added to every number's count so unseen numbers
        keep a non-zero chance.
    shape: when True, reject tickets whose sum / odd-count fall outside the
        historical central band before returning.
    """

    def __init__(self, *args, lookback=None, smoothing: float = 1.0, shape: bool = True, **kwargs):
        super().__init__(*args, **kwargs)
        self.lookback = lookback
        self.smoothing = smoothing
        self.shape = shape
        self._max_retries = 100

    def _weights(self, history):
        counts = Counter()
        for draw in history:
            counts.update(draw)
        return [counts.get(n, 0) + self.smoothing for n in range(self.min_val, self.max_val + 1)]

    @staticmethod
    def _band(values, low=0.1, high=0.9):
        if not values:
            return None
        ordered = sorted(values)
        n = len(ordered)
        lo = ordered[min(n - 1, int(low * n))]
        hi = ordered[min(n - 1, int(high * n))]
        return lo, hi

    def _passes(self, ticket, sum_band, odd_band):
        if not self.shape or sum_band is None:
            return True
        total = sum(ticket)
        odds = sum(1 for x in ticket if x % 2 == 1)
        return sum_band[0] <= total <= sum_band[1] and odd_band[0] <= odds <= odd_band[1]

    def predict(self, date=None):
        history = list(self._history_before(date))
        if not history:
            return sorted(random.sample(range(self.min_val, self.max_val + 1), self.number_predict))

        population = list(range(self.min_val, self.max_val + 1))
        weights = self._weights(history)

        sum_band = self._band([sum(d) for d in history])
        odd_band = self._band([sum(1 for x in d if x % 2 == 1) for d in history])

        best = None
        for _ in range(self._max_retries):
            picked = set()
            pool, pool_w = population[:], weights[:]
            while len(picked) < self.number_predict:
                choice = random.choices(pool, weights=pool_w, k=1)[0]
                idx = pool.index(choice)
                pool.pop(idx)
                pool_w.pop(idx)
                picked.add(choice)

            ticket = sorted(picked)
            best = ticket
            if self._passes(ticket, sum_band, odd_band):
                return ticket

        return best
