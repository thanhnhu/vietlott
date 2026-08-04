import pandas as pd

from vietlott.model.strategy.base import BaseStrategy
from vietlott.model.strategy.frequency import FrequencyStrategy


class RandomForestStrategy(BaseStrategy):
    """RandomForestRegressor fitted on past main numbers, seeded with frequency-weighted tickets.

    honest note: draws are independent, so this cannot beat the uniform baseline in
    expectation. kept for experimentation / comparison via ``backtest``.

    requires the optional ``ml`` extra: ``pip install vietlott-data[ml]``.
    """

    def __init__(self, *args, n_estimators: int = 200, **kwargs):
        super().__init__(*args, **kwargs)
        self.n_estimators = n_estimators

    def _matrix(self, date):
        hist = self._history_before(date)
        mat = pd.DataFrame(hist.tolist(), columns=[f"num_{i + 1}" for i in range(self.number_predict)])
        return mat.fillna(0).astype(int)

    def _sanitize(self, values):
        ticket, used = [], set()
        for v in values:
            v = max(self.min_val, min(self.max_val, int(round(v))))
            while v in used:
                v = v + 1 if v < self.max_val else self.min_val
            used.add(v)
            ticket.append(v)
        return sorted(ticket)

    def generate(self, date=None, n=1):
        from sklearn.ensemble import RandomForestRegressor

        # learn a mapping ticket -> ticket from past draws (X and y are the same matrix)
        mat = self._matrix(date)
        model = RandomForestRegressor(n_estimators=self.n_estimators, random_state=None)
        model.fit(mat, mat)

        # frequency-weighted tickets act as realistic inputs to feed the trained model
        seeder = FrequencyStrategy(self.df, min_val=self.min_val, max_val=self.max_val, shape=False)
        tickets = []
        for _ in range(n):
            seed = pd.DataFrame([seeder.predict(date)], columns=mat.columns)
            prediction = model.predict(seed)[0]
            # round/clip/dedupe the regressor output into a valid ticket
            tickets.append(self._sanitize(prediction))
        return tickets

    def predict(self, date=None):
        return self.generate(date, 1)[0]


if __name__ == "__main__":
    from vietlott.datasource import load_product

    df = load_product("power_655")
    model = RandomForestStrategy(df, min_val=1, max_val=55)
    for i, ticket in enumerate(model.generate(n=10), start=1):
        print(f"{i:02d}. {ticket}")
