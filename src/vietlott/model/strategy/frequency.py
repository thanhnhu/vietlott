import random
from collections import Counter

import pandas as pd

from vietlott.model.strategy.base import BaseStrategy


class FrequencyStrategy(BaseStrategy):
    """probability model over past draws: Laplace-smoothed frequency, distribution-shaped.

    by default it uses *every* past draw (``lookback=None``) to estimate each number's
    probability, then samples tickets from that distribution while keeping their sum and
    odd/even split inside the historical central band.

    honest note: draws are independent and uniform, so the *expected* return still equals
    the uniform baseline (see ``uniformity_test``). the edge is only cosmetic - generated
    tickets look like real draws. verify with ``backtest``/``evaluate``/``revenue``.

    parameters
    ----------
    lookback: number of most recent draws to weight by (``None`` = all past draws).
    smoothing: Laplace/Dirichlet prior added to every number's count so unseen numbers
        keep a non-zero probability.
    shape: when True, reject tickets whose sum / odd-count fall outside the historical
        central band before returning.
    """

    def __init__(self, *args, lookback=None, smoothing: float = 1.0, shape: bool = True, **kwargs):
        super().__init__(*args, **kwargs)
        self.lookback = lookback
        self.smoothing = smoothing
        self.shape = shape
        self._max_retries = 100

    def _history(self, date):
        hist = self._history_before(date)
        if self.lookback is not None:
            hist = hist.tail(self.lookback)
        return list(hist)

    def _counts(self, history):
        counts = Counter()
        for draw in history:
            counts.update(draw)
        return counts

    def number_probabilities(self, date=None) -> pd.Series:
        """Laplace-smoothed posterior probability of each number, estimated from history.

        each number's probability is ``(observed_count + smoothing) / total`` - this is the
        distribution the sampler draws from.
        """
        counts = self._counts(self._history(date))
        numbers = range(self.min_val, self.max_val + 1)
        weights = pd.Series({n: counts.get(n, 0) + self.smoothing for n in numbers}, dtype=float)
        return weights / weights.sum()

    def uniformity_test(self, date=None) -> dict:
        """chi-square goodness-of-fit test: do observed frequencies deviate from uniform?

        for a fair lottery this should NOT be significant (high p-value). ``p_value`` is
        included only when SciPy is installed; the statistic is always returned.
        """
        history = self._history(date)
        counts = self._counts(history)
        numbers = list(range(self.min_val, self.max_val + 1))
        total = sum(counts.get(n, 0) for n in numbers)
        expected = total / len(numbers) if numbers else 0.0
        chi_square = sum((counts.get(n, 0) - expected) ** 2 / expected for n in numbers) if expected else 0.0
        result = {
            "chi_square": chi_square,
            "dof": len(numbers) - 1,
            "expected_per_number": expected,
            "n_draws": len(history),
            "p_value": None,
        }
        try:
            from scipy import stats

            result["p_value"] = float(stats.chi2.sf(chi_square, result["dof"]))
        except ImportError:
            pass
        return result

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
        history = self._history(date)
        if not history:
            return sorted(random.sample(range(self.min_val, self.max_val + 1), self.number_predict))

        counts = self._counts(history)
        population = list(range(self.min_val, self.max_val + 1))
        weights = [counts.get(n, 0) + self.smoothing for n in population]

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
