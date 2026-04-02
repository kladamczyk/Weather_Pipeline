import requests
import json
from config import WeatherConfiguration

def fetch_past_weather_data(latitude, longitude, past_days) -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&daily="
            "weather_code,"
            "temperature_2m_max,temperature_2m_min,"
            "apparent_temperature_max,apparent_temperature_min,"
            "rain_sum,snowfall_sum"
        f"&past_days={past_days}"
        "&forecast_days=0"
        )
    try:
        response = requests.get(url)
        response.raise_for_status()

        weather_data = response.json()
        return weather_data
    except Exception as e:
        print(f"Unexpected {e}")

def main():
    city = WeatherConfiguration.DEFAULT_CITY
    latitude = WeatherConfiguration.DEFAULT_LATITUDE
    longitude = WeatherConfiguration.DEFAULT_LATITUDE
    past_days = WeatherConfiguration.DEFAULT_PAST_DAYS
    with open("weather_past_data.json", "w") as file:
        json.dump(fetch_past_weather_data(latitude, longitude, past_days), file, indent=4)
        print(f"Succesfully aquired past weather data in {city}.")
    file.close()

if __name__ == "__main__":
    main()