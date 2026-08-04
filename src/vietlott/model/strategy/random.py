import random

from vietlott.model.strategy.base import BaseStrategy


class RandomStrategy(BaseStrategy):
    """uniform baseline: pick ``number_predict`` distinct numbers in ``[min_val, max_val]``."""

    def predict(self, *args, **kwargs):
        nums = list(range(self.min_val, self.max_val + 1))
        random.shuffle(nums)
        return sorted(nums[: self.number_predict])
