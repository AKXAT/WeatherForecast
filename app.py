from flask import Flask, render_template
from backend import main as weather_methods

app = Flask(__name__)


@app.route("/<city>")
def index(city):
    current_weather = weather_methods.get_current_temprature(city=city)
    return render_template("homepage.html", current_weather=current_weather)


app.run(debug=True)
