from flask import Flask, render_template, request
from backend import main as weather_methods

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return weather_page(request.form["city"])
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


app.run(debug=True)
