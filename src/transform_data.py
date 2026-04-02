import pandas as pd
import json

def read_file(file):
    try:
        with open(file, "r") as file:
            data = json.load(file)
            print(type(data))
        return data
    except Exception as e:
        print(f"Unexpected {e}")

def transform_data(data) -> pd.DataFrame:
    try:
        df = pd.DataFrame(data["daily"])
        df.columns = [
                    "date", "weather_code", "max_temperature", "min_temperature", 
                    "max_apparent_temperature", "min_apparent_temperature", "rain_sum", "snowfall_sum"
                    ]

        df.ffill(inplace=True)
        df.dropna(inplace=True)
        df = df.reset_index(drop=True)

        df["date"] = pd.to_datetime(df["date"])
        df["weather_code"] = df["weather_code"].astype(int)

        return df
    except Exception as e:
        print(f"Unexpected {e}")

def main():
    data_weather = read_file('weather_past_data.json')
    transformed_weather = transform_data(data_weather)
    transformed_weather.to_csv("transformed_weather_data.csv", index=False)

if __name__ == "__main__":
    main()