import numpy as np
import pandas as pd

from vietlott.model.strategy.base import BaseStrategy


class LSTMStrategy(BaseStrategy):
    """LSTM sequence model over past draws (ported from the original TensorFlow predictor).

    honest note: draws are independent, so this cannot beat the uniform baseline in
    expectation. kept for experimentation / comparison via ``backtest``.

    requires the optional ``ml`` extra: ``pip install vietlott-data[ml]``.
    """

    def __init__(self, *args, epochs: int = 100, **kwargs):
        super().__init__(*args, **kwargs)
        self.epochs = epochs

    def _matrix(self, date):
        hist = self._history_before(date)
        mat = pd.DataFrame(hist.tolist())
        return mat.fillna(0).astype(int)

    def _build_model(self, num_features, max_value):
        from keras import layers
        from tensorflow import keras

        model = keras.Sequential()
        model.add(layers.Embedding(input_dim=max_value + 1, output_dim=128))
        model.add(layers.LSTM(128))
        model.add(layers.Dense(num_features, activation="softmax"))
        model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
        return model

    def generate(self, date=None, n=1):
        from tensorflow import keras

        data = self._matrix(date)
        train_data = data[: int(0.8 * len(data))]
        val_data = data[int(0.8 * len(data)) :]
        max_value = int(np.max(data.values))
        num_features = int(train_data.shape[1])

        model = self._build_model(num_features, max_value)
        early_stopping = keras.callbacks.EarlyStopping(
            monitor="val_loss", patience=10, restore_best_weights=True, verbose=0
        )
        model.fit(
            train_data,
            train_data,
            validation_data=(val_data, val_data),
            epochs=self.epochs,
            callbacks=[early_stopping],
            verbose=0,
        )

        predictions = model.predict(val_data, verbose=0)
        indices = np.argsort(predictions, axis=1)[:, -num_features:]
        picked = np.take_along_axis(val_data.to_numpy(), indices, axis=1)
        return [sorted(int(x) for x in row) for row in picked[:n]]

    def predict(self, date=None):
        return self.generate(date, 1)[0]


if __name__ == "__main__":
    import os

    os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
    from vietlott.datasource import load_product

    df = load_product("power_655")
    model = LSTMStrategy(df, min_val=1, max_val=55)
    for i, ticket in enumerate(model.generate(n=2), start=1):
        print(f"{i:02d}. {ticket}")
