from dotenv import load_dotenv
import os

load_dotenv()

class WeatherConfiguration:
    DATABASE_URL = os.getenv("DATABASE_URL")

    DEFAULT_LATITUDE = 52.13
    DEFAULT_LONGITUDE = 21.00
    DEFAULT_CITY = 'Warsaw'
    DEFAULT_PAST_DAYS = 92