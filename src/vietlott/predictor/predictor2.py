import os, sys
# disable tensorflow warnings/messages
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
#os.environ['PYCARET_CUSTOM_LOGGING_LEVEL'] = 'CRITICAL'

import pandas as pd
import numpy as np
from tensorflow import keras
from keras import layers

sys.path.append(os.path.dirname(os.path.abspath('src/vietlott')))
from vietlott.config.products import get_config


class Predictor2():
    def predict(self, df, number_of_tickets = 1, time_id = None):
        if(time_id is not None):
            df = df[df.id < time_id].copy(deep=True)

        # Prepare the data
        df["date"] = pd.to_datetime(df["date"]).dt.date
        data = df.sort_values(by=["date", "id"], ascending=True)
        data = data["result"]
        if len(data[0]) == 7:  # Remove last column
            for r in data: del r[-1]
        data = pd.DataFrame(data.values.tolist())
        data.fillna(0, inplace=True)
        data = data.apply(lambda x: x.astype(int))
        #print(data)

        # Split data into training and validation sets
        train_data = data[:int(0.8*len(data))]
        val_data = data[int(0.8*len(data)):]
        # Get the maximum value in the data
        max_value = np.max(data)
        
        # Get number of features from training data 
        num_features = train_data.shape[1]

        # Create and compile model 
        model = self.create_model(num_features, max_value)

        # Train model
        self.train_model(model, train_data, val_data)
        
        # Predict numbers using trained model
        res = []
        i = 0
        while i < number_of_tickets:
            predict_numbers = self.predict_numbers(model, val_data, num_features)
            res.append(predict_numbers[0])
            i += 1
        #print(f"res: {res}")
        #res = np.vstack(res)
        res = np.sort(res, axis=1)

        return pd.DataFrame(res)

    # Function to create the model
    def create_model(self, num_features, max_value):
        # Create a sequential model
        model = keras.Sequential()
        # Add an Embedding layer, LSTM layer, and Dense layer to the model
        model.add(layers.Embedding(input_dim=max_value+1, output_dim=128))
        model.add(layers.LSTM(128))
        model.add(layers.Dense(num_features, activation='softmax'))
        # Compile the model with categorical crossentropy loss, adam optimizer, and accuracy metric
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    # Function to train the model
    def train_model(self, model, train_data, val_data):
        # Add early stopping to prevent overfitting
        early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
        # Fit the model on the training data and validate on the validation data
        model.fit(train_data, train_data, validation_data=(val_data, val_data), epochs=100, callbacks=[early_stopping])

    # Function to predict numbers using the trained model
    def predict_numbers(self, model, val_data, num_features):
        batch_size = 32
        predictions = []
        for i in range(0, len(val_data), batch_size):
            batch_predictions = model.predict(val_data[i:i+batch_size])
            predictions.append(batch_predictions)
        predictions = np.vstack(predictions)
        # Predict on the validation data using the model
        predictions = model.predict(val_data)
        # Get the indices of the top 'num_features' predictions for each sample in validation data
        indices = np.argsort(predictions, axis=1)[:, -num_features:]
        
        # Get the predicted numbers using these indices from validation data
        val_data_np = val_data.to_numpy()
        predicted_numbers = np.take_along_axis(val_data_np, indices, axis=1)
        return predicted_numbers

if __name__ == "__main__":
    # Load the data from json file
    df = pd.read_json(get_config("power_655").raw_path, lines=True, dtype=object, convert_dates=False)
    #predict = Predictor2().predict(df, 1, '00020')
    predict = Predictor2().predict(df, 1)
    for index, row in predict.iterrows():
        print(str(f"{index+1:02d}") + ". ", row.tolist())