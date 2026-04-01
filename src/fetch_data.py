import requests
import json

def fetch_weather_data():
    url = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=weather_code,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,daylight_duration,sunset,sunrise,uv_index_max,rain_sum,snowfall_sum,wind_speed_10m_max,sunshine_duration&past_days=31"
    
    response = requests.get(url)

    #TUTAJ TRZEBA DODAĆ ERROR HANDLING
    weather_data = response.json()
    return weather_data


#ZAPISUJE DANE DO PLIKU JSON
with open("weather_data.json", "w") as file:
    json.dump(fetch_weather_data(), file, indent=4)
