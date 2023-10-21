import requests
import json

url = "https://api.open-meteo.com/v1/forecast"


def get_lat_long(city_name: str) -> any:
    # Open the JSON file for reading
    with open("backend/cities.json", "r+") as json_file:
        # Load the JSON data from the file into a Python dictionary
        data = json.load(json_file)

    # Access the city information from the parsed data
    cities = data["cities"]

    # Loop through the cities and print their names and coordinates
    count = 0
    for city in cities:
        if city["name"].replace(" ", "").upper() == city_name.replace(" ", "").upper():
            count += 1
            return city["latitude"], city["longitude"]

    if count == 0:
        return None, None


def get_current_temprature(city: str) -> any:
    lat, long = get_lat_long(city_name=city)
    if lat is None or long is None:
        return None
    params = {
        "latitude": lat,
        "longitude": long,
        "current": "temperature_2m,weathercode",
    }
    first = requests.get(url=url, params=params)
    return first.json()


def get_5days_temprature(city: str) -> any:
    lat, long = get_lat_long(city_name=city)
    if lat is None or long is None:
        return None
    params = {
        "latitude": lat,
        "longitude": long,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "GMT",
        "forecast_days": "5",
    }
    first = requests.get(url=url, params=params)
    return first.json()


def weather_code(code: int) -> str:
    if code == 0:
        return "🌈 Clear Sky"
    elif code == 1:
        return "🌄 Mainly Clear"
    elif code == 2:
        return "⛅️ Partly Cloudy"
    elif code == 45:
        return "🌁 Fog"
    elif code == 48:
        return "😶‍🌫️ Depositing Rime Fog"
    elif code == 51:
        return "🌧️ Light Drizzle"
    elif code == 53:
        return "☔️ Moderate Drizzle"
    elif code == 55:
        return "⛈️ Heavy Drizzle"
    elif code == 61:
        return "🌦️ Slight Rain"
    elif code == 63:
        return "🌧️ Moderate Rain"
    elif code == 65:
        return "⛈️ Heavy Rain"
    elif code == 71:
        return "❅ Slight Snowfall"
    elif code == 73:
        return "⛄️ Moderate Snowfall"
    elif code == 75:
        return "☃️ Heavy Snowfall"
    elif code == 77:
        return "❄️ Snow grains"
    elif code == 80:
        return "💧 Slight Rain Showers"
    elif code == 81:
        return "☔︎ Moderate Rain Showers"
    elif code == 82:
        return "⛈ Violent Rain Showers"
    elif code == 85:
        return "🏂 Slight Snow Showers"
    elif code == 86:
        return "☃️ Heavy Snow Showers"
    elif code == 95:
        return "⚡️ Thunderstorm"
    elif code == 96:
        return "🌊 Thunderstorm with Slight Hail"
    elif code == 99:
        return "🌊 Thunderstorm with Heavy Hail"
    else:
        return "🌱 Pleasent Day"


def choose_emoji(tempratrue: float, actual_weather_code=100) -> str:
    if 0 < tempratrue < 15:
        return "❄️ " + weather_code(actual_weather_code)
    elif 15 < tempratrue < 25:
        return "🌤️ " + weather_code(actual_weather_code)
    elif 25 < tempratrue < 35:
        return "☀️ " + weather_code(actual_weather_code)
    elif tempratrue > 35:
        return "🔥 " + weather_code(actual_weather_code)
    elif tempratrue < 0:
        return "☃️ " + weather_code(actual_weather_code)
    else:
        return "⚠️" + weather_code(actual_weather_code)
