import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from random import randint, choices
from loguru import logger
#from datetime import datetime, timedelta
#from io import StringIO
#from pathlib import Path

import os, sys
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#print(os.path.dirname(os.path.abspath('src/vietlott')))
sys.path.append(os.path.dirname(os.path.abspath('src/vietlott')))
from vietlott.config.products import get_config


class Predictor():
    def predict(self, df, number_of_ticket, time_id = None, name = None):
        logger.info(f"predict by RandomForestRegressor")
        if(time_id is not None):
            df = df[df.id < time_id].copy(deep=True)

        df["date"] = pd.to_datetime(df["date"]).dt.date
        data = df.sort_values(by=["date", "id"], ascending=True)
        #print(data.head(10))
        data = data["result"]
        if len(data[0]) == 7:  # Remove last column
            for r in data: del r[-1]
        data = pd.DataFrame(data.values.tolist(), columns= ["num_%d" % (i+1) for i in range(6)])
        data.fillna(0, inplace=True)
        data = data.apply(lambda x: x.astype(int))

        res = []
        i = 0
        while i < number_of_ticket:
            # Split the data into features (X) and target (y)
            X = data[['num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6']]
            y = data.iloc[:, :]

            # Train a Random Forest Regression model
            #model = RandomForestRegressor(n_estimators=1000, random_state=None)
            model = RandomForestRegressor(n_estimators=data.shape[0], random_state=None)
            model.fit(X, y)

            # Generate a new set of random features for prediction
            # new_data = pd.DataFrame({
            #     "num_1": [randint(1, 50) for _ in range(100)],
            #     "num_2": [randint(2, 51) for _ in range(100)],
            #     "num_3": [randint(3, 52) for _ in range(100)],
            #     "num_4": [randint(4, 53) for _ in range(100)],
            #     "num_5": [randint(5, 54) for _ in range(100)],
            #     "num_6": [randint(6, 55) for _ in range(100)],
            # })
            new_ticket = self.fn_random_ticket_645(df, 1) \
                if name is not None and name == "power_645" \
                else self.fn_random_ticket_655(df, 1)
            new_data = pd.DataFrame(new_ticket.values.tolist(), columns= ["num_%d" % (i+1) for i in range(6)])

            # Use the trained model to predict the next 6 numbers for each set of features
            predictions = model.predict(new_data)

            # Convert predictions to whole numbers
            predictions = [[round(i) for i in p] for p in predictions]
            #print(predictions)
            
            # # Select first number each row
            # arr_first_number = np.array(predictions)[:, 0]
            # # Group by the same first number & count
            # rows, count = np.unique(arr_first_number, return_counts = True)
            
            # # Select rows prioritize have count of first number = 2, it will happen again
            # repeated = []
            # for p in predictions:
            #     y = rows[count == 2]
            #     if(y.size != 0 and y[0] == p[0]):
            #         repeated.append(p)

            # check_column = 0
            # if(len(repeated) >= 2):
            #     predictions = repeated
            #     check_column = 1
            # # Select closest row
            # a = min(np.array(predictions)[:,0])
            # b = max(np.array(predictions)[:,0])
            # chunk_size = (b-a) / 2
            # index = a + chunk_size
            # res.append(min(predictions, key=lambda x:abs(x[check_column]-index)))
            res.append(predictions[0])

            i += 1

        return pd.DataFrame(res)
        #return pd.concat([new_ticket, pd.DataFrame(res)], ignore_index=True)

    def fn_random_ticket_655(self, df, number_of_ticket):
        res = []
        i = 0
        while i < number_of_ticket:
            item = []
            # Number 1
            population = list(range(1, 50 + 1))
            #weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]
            num1 = self.fn_random_number(df, 1, population)
            item.append(num1[0])

            # Number 2
            population = list(range(num1[0] + 1, 51 + 1))
            num2 = self.fn_random_number(df, 2, population)
            item.append(num2[0])

            # Number 3
            population = list(range(num2[0] + 1, 52 + 1))
            num3 = self.fn_random_number(df, 3, population)
            item.append(num3[0])

            # Number 4
            population = list(range(num3[0] + 1, 53 + 1))
            num4 = self.fn_random_number(df, 4, population)
            item.append(num4[0])

            # Number 5
            population = list(range(num4[0] + 1, 54 + 1))
            num5 = self.fn_random_number(df, 5, population)
            item.append(num5[0])

            # Number 6
            population = list(range(num5[0] + 1, 55 + 1))
            num6 = self.fn_random_number(df, 6, population)
            item.append(num6[0])

            res.append(item)
            i += 1

        return pd.DataFrame(res)

    def fn_random_ticket_645(self, df, number_of_ticket):
        res = []
        i = 0
        while i < number_of_ticket:
            item = []
            # Number 1
            population = list(range(1, 40 + 1))
            #weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]
            num1 = self.fn_random_number(df, 1, population)
            item.append(num1[0])

            # Number 2
            population = list(range(num1[0] + 1, 41 + 1))
            num2 = self.fn_random_number(df, 2, population)
            item.append(num2[0])

            # Number 3
            population = list(range(num2[0] + 1, 42 + 1))
            num3 = self.fn_random_number(df, 3, population)
            item.append(num3[0])

            # Number 4
            population = list(range(num3[0] + 1, 43 + 1))
            num4 = self.fn_random_number(df, 4, population)
            item.append(num4[0])

            # Number 5
            population = list(range(num4[0] + 1, 44 + 1))
            num5 = self.fn_random_number(df, 5, population)
            item.append(num5[0])

            # Number 6
            population = list(range(num5[0] + 1, 45 + 1))
            num6 = self.fn_random_number(df, 6, population)
            item.append(num6[0])

            res.append(item)
            i += 1

        return pd.DataFrame(res)

    def fn_random_number(self, df, col_number, population):
        count_percent = self.fn_count_percentage(df, col_number)
        existing_numbers = list(count_percent.index)
        weights = []
        for p in population:
            if(p in existing_numbers):
                weights.append(count_percent.loc[p,"%"] / 100)
            else:
                weights.append(0)

        random = choices(population, weights)
        return random

    def fn_count_percentage(self, df, col_number, count_time=None):
        #df["date"] = pd.to_datetime(df["date"]).dt.date
        df = df.sort_values(by=["date", "id"], ascending=True)

        if count_time is not None:
            df = df.tail(count_time) # Get last results by count_time

        # Get all numbers by column index
        data = df["result"]
        if len(data[0]) == 7:  # Remove last column
            for r in data: del r[-1]
        data = pd.DataFrame(data.values.tolist(), columns= ["%d" % (i+1) for i in range(6)])
        #data = data.iloc[:, col_number-1]
        data.fillna(0, inplace=True)
        data = data.apply(lambda x: x.astype(int))

        stats = data.groupby("%d" % col_number).agg(count=("%d" % col_number, 'count'))
        stats['%'] = (stats['count'] / len(data) * 100).round(2)
        #print(stats)
        return stats

if __name__ == "__main__":
    # Load the data from json file
    df = pd.read_json(get_config("power_655").raw_path, lines=True, dtype=object, convert_dates=False)
    predict = Predictor().predict(df, 10, '01025')
    #predict = Predictor().predict(df, 10)
    #random_ticket = Predictor().fn_random_ticket(df, 10)
    for index, row in predict.iterrows():
        print(str(f"{index+1:02d}") + ". ", row.tolist())
    #for index, row in random_ticket.iterrows():
    #    print(str(f"{index+1:02d}") + ". ", row.tolist())