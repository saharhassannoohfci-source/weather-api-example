"""Fetch current weather using an API key from .env."""

import os
import sys
from dataclasses import dataclass
from pathlib import Path

import requests
from dotenv import load_dotenv


@dataclass
class Weather:
    city: str
    country: str
    condition: str
    temperature_c: float
    humidity: int

    def summary(self) -> str:
        return (
            f"Weather in {self.city}, {self.country}\n"
            f"{'-' * 36}\n"
            f"Condition:   {self.condition}\n"
            f"Temperature: {self.temperature_c:.1f} C\n"
            f"Humidity:    {self.humidity}%"
        )


def main() -> int:
    load_dotenv(Path(__file__).with_name(".env"))
    api_key = os.getenv("WEATHER_API_KEY", "").strip()
    if not api_key or api_key == "your_api_key_here":
        print("Add your WeatherAPI key to WEATHER_API_KEY in .env.", file=sys.stderr)
        return 1

    city = " ".join(sys.argv[1:]) or os.getenv("WEATHER_CITY", "Cairo")
    try:
        response = requests.get(
            "https://api.weatherapi.com/v1/current.json",
            params={"key": api_key, "q": city, "aqi": "no"},
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
        weather = Weather(
            city=data["location"]["name"],
            country=data["location"]["country"],
            condition=data["current"]["condition"]["text"],
            temperature_c=float(data["current"]["temp_c"]),
            humidity=int(data["current"]["humidity"]),
        )
    except requests.HTTPError as error:
        print(f"API request failed (HTTP {error.response.status_code}). Check your key and city.", file=sys.stderr)
        return 1
    except requests.RequestException:
        print("Could not reach the weather API. Check your connection and try again.", file=sys.stderr)
        return 1
    except (KeyError, TypeError, ValueError):
        print("The API returned an unexpected JSON response.", file=sys.stderr)
        return 1

    print(weather.summary())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
