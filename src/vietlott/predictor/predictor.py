import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from random import randint
#from datetime import datetime, timedelta
#from io import StringIO
#from pathlib import Path

import os, sys
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#print(os.path.dirname(os.path.abspath('src/vietlott')))
sys.path.append(os.path.dirname(os.path.abspath('src/vietlott')))
from vietlott.config.products import get_config


class Predictor():
    def predict(self, data, number_of_ticket):
        #data.fillna(0, inplace=True)
        #print(data.head(10))
        res = []
        i = 0
        while i < number_of_ticket: 
            # Split the data into features (X) and target (y)
            X = data[['num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6']]
            y = data.iloc[:, :-1] # Remove last column
            #print(X)
            #print(y)

            # Train a Random Forest Regression model
            #model = RandomForestRegressor(n_estimators=1000, random_state=None)
            model = RandomForestRegressor(n_estimators=data.shape[0], random_state=None)
            model.fit(X, y)

            # Generate a new set of random features for prediction
            new_data = pd.DataFrame({
                "num_1": [randint(1, 10) for _ in range(100)],
                "num_2": [randint(2, 51) for _ in range(100)],
                "num_3": [randint(3, 52) for _ in range(100)],
                "num_4": [randint(4, 53) for _ in range(100)],
                "num_5": [randint(5, 54) for _ in range(100)],
                "num_6": [randint(6, 55) for _ in range(100)],
            })

            # Use the trained model to predict the next 6 numbers for each set of features
            predictions = model.predict(new_data)

            # Get the most likely set of numbers based on the predictions
            most_likely_set = predictions[0]
            for p in predictions:
                if p[0] > most_likely_set[0]:
                    most_likely_set = p

            # Convert most_likely_set to whole numbers
            rounded_most_likely_set = [round(x) for x in most_likely_set]

            # Print the most likely set of numbers
            res.append(rounded_most_likely_set)
            #print(str(f"{i+1:02d}") + ". The most likely set of numbers is:", rounded_most_likely_set)
            i += 1

        return pd.DataFrame(res)

if __name__ == "__main__":
    # Load the data from json file
    df = pd.read_json(get_config("power_655").raw_path, lines=True, dtype=object, convert_dates=False)
    #df["date"] = pd.to_datetime(df["date"]).dt.date
    #df = df.sort_values(by=["date", "id"], ascending=False)
    data = df["result"]
    #print(data.head(10))
    data = pd.DataFrame(data.values.tolist(), columns= ["num_%d" % (i+1) for i in range(7)])
    #data.fillna(0, inplace=True)
    predict = Predictor().predict(data, 10)
    #print(type(predict))
    #print(predict)
    #predict = predict.reset_index()
    for index, row in predict.iterrows():
        print(str(f"{index+1:02d}") + ". The most likely set of numbers is:", row.tolist())