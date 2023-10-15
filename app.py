from flask import Flask, render_template
from backend import main as weather_methods

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("base.html")


@app.route("/<city>")
def weather_page(city):
    current_weather = weather_methods.get_current_temprature(city=city)
    return render_template("weather.html", current_weather=current_weather)


app.run(debug=True)
