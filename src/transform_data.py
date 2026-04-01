import pandas as pd
import json

#TUTAJ TRZEBA OGARNAC ERROR HANDLING
def read_file(file):
    with open(file, "r") as file:
        data = json.load(file)
    return data

#ERROR HANDLING!!!
def transform_data(data):
    df = pd.DataFrame(data["daily"])
    print(df)
    #zmien nazwy kolumn tutaj

    #zmien typ danych na poprawne
    df["time"] = pd.to_datetime(df["time"])

    #ogarnij case jakby byly missing values

    print(df.isnull().sum()) #sprawdza, czy jakiekolwiek wartosci sa null
    #print(df.columns)

r = read_file('weather_data.json')
result = transform_data(r)
#print(result)