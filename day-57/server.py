import random, requests
from datetime import datetime
from flask import Flask, render_template

GENDERIZE_URL = "https://api.genderize.io"
AGIFY_URL = "https://api.agify.io"

app = Flask(__name__)


@app.route("/")
def home():
    number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    params = {
        "name": name
    }
    genderize_response = requests.get(url=GENDERIZE_URL, params=params)
    genderize_response.raise_for_status()
    gender = genderize_response.json()["gender"]

    agify_response = requests.get(url=AGIFY_URL, params=params)
    agify_response.raise_for_status()
    age = agify_response.json()["age"]

    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
