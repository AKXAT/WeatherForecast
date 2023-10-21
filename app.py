from flask import Flask, render_template, request
from backend import main as weather_methods

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        action = request.form["action"]
        city = request.form["city"]

        if action == "current":
            return weather_page(city)
        elif action == "prediction":
            return weather_5days(city)

    return render_template("base.html")


@app.route("/<city>")
def weather_page(city):
    actual_weather_code = 100
    weather_call = weather_methods.get_current_temprature(city=city)
    if weather_call is None:
        _str = "No Data Avaliable"
        return render_template(
            "weather.html", lat=_str, long=_str, current_weather=_str, emoji="❌"
        )
    lat = weather_call.get("latitude")
    long = weather_call.get("longitude")
    current_weather = weather_call.get("current").get("temperature_2m")
    weather_code = weather_call.get("current").get("weathercode")
    if weather_code is not None:
        actual_weather_code = weather_code
    emoji = weather_methods.choose_emoji(
        current_weather, actual_weather_code=actual_weather_code
    )
    return render_template(
        "weather.html", lat=lat, long=long, current_weather=current_weather, emoji=emoji
    )


@app.route("/5days")
def weather_5days(city):
    weather_call = weather_methods.get_5days_temprature(city=city)
    if weather_call is None:
        _str = "No Data Available"
        return render_template(
            "weather_5d.html",
            lat=_str,
            long=_str,
            daily_date=[],
            daily_max_temperature=[],
            daily_min_temperature=[],
            date_length=0,  # Set to 0 if no data is available
        )

    lat = weather_call["latitude"]
    long = weather_call["longitude"]
    daily_date = weather_call["daily"]["time"]
    daily_max_temperature = weather_call["daily"]["temperature_2m_max"]
    daily_min_temperature = weather_call["daily"]["temperature_2m_min"]
    date_length = len(daily_date)

    return render_template(
        "weather_5d.html",
        lat=lat,
        long=long,
        daily_date=daily_date,
        daily_max_temperature=daily_max_temperature,
        daily_min_temperature=daily_min_temperature,
        date_length=date_length,
    )


app.run(debug=True)
