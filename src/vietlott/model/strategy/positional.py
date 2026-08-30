import math
import random
from collections import Counter

from vietlott.model.strategy.base import BaseStrategy


class PositionalStrategy(BaseStrategy):
    """predict each sorted position (order statistic) separately, then assemble ascending tickets.

    the draw is stored sorted, so position ``k`` (the k-th smallest number) has its own
    distribution: position 0 tends to be small, the last tends to be large. this strategy models
    each column independently with a pluggable ``column_model`` and samples numbers left-to-right
    under the constraint ``num[k] > num[k-1]``.

    ``column_model``:
      - ``"frequency"``   : per-column value histogram (light, no extra deps).
      - ``"random_forest"``: per-column regressor on the previous draw (needs ``ml`` extra).
      - ``"lstm"``        : per-column sequence model (needs ``ml`` extra, heavy).

    honest note: draws are independent and uniform, so this does not beat the random baseline in
    expectation - it only produces better-shaped tickets. verify with ``backtest`` / ``revenue``.
    """

    _MODELS = ("frequency", "random_forest", "lstm")

    def __init__(
        self,
        *args,
        column_model: str = "frequency",
        smoothing: float = 1.0,
        n_estimators: int = 100,
        epochs: int = 30,
        window: int = 10,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        if column_model not in self._MODELS:
            raise ValueError(f"column_model={column_model!r} must be one of {self._MODELS}")
        self.column_model = column_model
        self.smoothing = smoothing
        self.n_estimators = n_estimators
        self.epochs = epochs
        self.window = window

    # --- per-column weight functions (one per position) ---------------------------------

    def _column_predictors(self, history):
        cols = [[draw[k] for draw in history] for k in range(self.number_predict)]
        if self.column_model == "frequency":
            return [self._freq_weight(Counter(col)) for col in cols]
        if self.column_model == "random_forest":
            return self._rf_weights(history, cols)
        return self._lstm_weights(cols)

    def _freq_weight(self, counter):
        return lambda v: counter.get(v, 0) + self.smoothing

    @staticmethod
    def _gauss_weight(mean, std):
        std = max(std, 1.0)
        return lambda v: math.exp(-0.5 * ((v - mean) / std) ** 2)

    def _rf_weights(self, history, cols):
        import numpy as np
        from sklearn.ensemble import RandomForestRegressor

        # predict this draw's column k from the previous draw's numbers
        x = np.array(history[:-1])
        last = np.array(history[-1]).reshape(1, -1)
        weights = []
        for col in cols:
            y = np.array(col[1:])
            model = RandomForestRegressor(n_estimators=self.n_estimators, random_state=None)
            model.fit(x, y)
            tree_preds = np.array([est.predict(last)[0] for est in model.estimators_])
            weights.append(self._gauss_weight(float(tree_preds.mean()), float(tree_preds.std())))
        return weights

    def _lstm_weights(self, cols):
        import numpy as np

        w = self.window
        weights = []
        for col in cols:
            arr = np.array(col, dtype=float)
            std = float(arr.std())
            if len(arr) <= w:  # not enough history to train a sequence model
                weights.append(self._gauss_weight(float(arr.mean()), std))
                continue

            from keras import layers
            from tensorflow import keras

            x = np.array([arr[i : i + w] for i in range(len(arr) - w)]).reshape(-1, w, 1) / self.max_val
            y = np.array([arr[i + w] for i in range(len(arr) - w)]) / self.max_val
            model = keras.Sequential([layers.Input((w, 1)), layers.LSTM(16), layers.Dense(1)])
            model.compile(loss="mse", optimizer="adam")
            model.fit(x, y, epochs=self.epochs, verbose=0)
            last_window = (arr[-w:].reshape(1, w, 1)) / self.max_val
            pred = float(model.predict(last_window, verbose=0)[0, 0]) * self.max_val
            weights.append(self._gauss_weight(pred, std))
        return weights

    # --- sampling ------------------------------------------------------------------------

    def _sample_ticket(self, weight_fns):
        ticket = []
        prev = self.min_val - 1
        for k in range(self.number_predict):
            hi = self.max_val - (self.number_predict - 1 - k)  # leave room for the remaining numbers
            feasible = list(range(prev + 1, hi + 1))
            w = [max(weight_fns[k](v), 0.0) for v in feasible]
            choice = random.choices(feasible, weights=w, k=1)[0] if sum(w) > 0 else random.choice(feasible)
            ticket.append(choice)
            prev = choice
        return ticket

    def generate(self, date=None, n=1):
        history = list(self._history_before(date))
        if len(history) < 2:  # nothing to learn from
            return [self._sample_ticket([lambda v: 1.0] * self.number_predict) for _ in range(n)]
        weight_fns = self._column_predictors(history)
        return [self._sample_ticket(weight_fns) for _ in range(n)]

    def predict(self, date=None):
        return self.generate(date, 1)[0]


if __name__ == "__main__":
    from vietlott.datasource import load_product

    df = load_product("power_655")
    for model_name in PositionalStrategy._MODELS:
        print(f"== {model_name} ==")
        model = PositionalStrategy(df, column_model=model_name, min_val=1, max_val=55)
        for i, ticket in enumerate(model.generate(n=3), start=1):
            print(f"{i:02d}. {ticket}")
