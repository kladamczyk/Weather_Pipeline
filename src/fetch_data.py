import requests
import json

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

def fetch_weather_forecast_data(latitude, longitude, forecast_days) -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&daily="
            "weather_code,"
            "temperature_2m_max,temperature_2m_min,"
            "apparent_temperature_max,apparent_temperature_min,"
            "rain_sum,snowfall_sum"
        f"&forecast_days={forecast_days}"
        )
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        weather_data = response.json()
        return weather_data
    except Exception as e:
        print(f"Unexpected {e}")

def main():
    with open("weather_past_data.json", "w") as file:
        json.dump(fetch_past_weather_data(52.13, 21.00, 92), file, indent=4)

    with open("weather_forecast_data.json", "w") as file:
        json.dump(fetch_weather_forecast_data(52.13, 21.00, 16), file, indent=4)

if __name__ == "__main__":
    main()