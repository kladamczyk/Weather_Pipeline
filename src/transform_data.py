import pandas as pd
import json

#TUTAJ TRZEBA OGARNAC ERROR HANDLING
def read_file(file):
    with open(file, "r") as file:
        data = json.load(file)
    return data

#ERROR HANDLING!!!
def transform_data(data) -> pd.DataFrame:
    try:
        df = pd.DataFrame(data["daily"])
        df.columns = [
                    "date", "weather_code", "max_temperature", "min_temperature", "max_apparent_temperature",
                    "min_apparent_temperature", "sunset_time", "sunrise_time", "rain_sum", "snowfall_sum"
                    ]

        df.fillna(method='pad', inplace=True)
        df.dropna(inplace=True)
        df = df.reset_index(drop=True)

        df["date"] = pd.to_datetime(df["date"])
        df["weather_code"] = df["weather_code"].astype(int)
        df["sunset_time"] = pd.to_datetime(df["sunset_time"]).dt.time
        df["sunrise_time"] = pd.to_datetime(df["sunrise_time"]).dt.time

        return df
    except:
        print("Boo hoo")

def main():
    data_weather_forecast = read_file('weather_forecast_data.json')
    data_weather_past = read_file('weather_past_data.json')

    transformed_weather_forecast = transform_data(data_weather_forecast)
    transformed_weather_past = transform_data(data_weather_past)

    transformed_weather_forecast.to_csv("transformed_weather_forecast_data.csv", index=False)
    transformed_weather_past.to_csv("transformed_weather_past_data.csv", index=False)

if __name__ == "__main__":
    main()