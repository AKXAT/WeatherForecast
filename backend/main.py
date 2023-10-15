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
    params = {"latitude": lat, "longitude": long, "current": "temperature_2m"}
    first = requests.get(url=url, params=params)
    return first.json()
