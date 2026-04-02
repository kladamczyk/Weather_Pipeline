import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base, Session
from config import WeatherConfiguration

Base = declarative_base()

class WeatherDatabase(Base):
    __tablename__ = "weather_database"

    date = Column(DateTime, primary_key=True)
    weather_code = Column(Integer, nullable=False)
    max_temperature = Column(Float, nullable=False)
    min_temperature = Column(Float, nullable=False)
    max_apparent_temperature = Column(Float, nullable=False)
    min_apparent_temperature = Column(Float, nullable=False)
    rain_sum = Column(Float, nullable=False)
    snowfall_sum = Column(Float, nullable=False)

def create_database():
    try:
        engine = create_engine(f"{WeatherConfiguration.DATABASE_URL}")
        Base.metadata.create_all(engine)
        return engine
    except Exception as e:
        print(f"Unexpected {e}")

def load_data_to_database(df):
    engine = create_database()

    try:
        df["date"] = pd.to_datetime(df["date"])

        existing_dates = pd.read_sql("SELECT date FROM weather_database", Session(engine).bind)
        existing_dates_set = set(existing_dates["date"])

        new_df = df[~df["date"].isin(existing_dates_set)]
        if not new_df.empty:
            new_df.to_sql("weather_database", engine, if_exists="append", index=False)
        return True
    except Exception as e:
        print(f"Unexpected {e}")

def main():
    df = pd.read_csv("transformed_weather_data.csv")
    b = load_data_to_database(df)
    if b:
        print("Succesfully loaded weather data to database.")

if __name__ == "__main__":
    main()