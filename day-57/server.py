import random, requests
from datetime import datetime
from flask import Flask, render_template

GENDERIZE_URL = "https://api.genderize.io"
AGIFY_URL = "https://api.agify.io"
NPOINT_URL = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)


@app.route("/")
def home():
    number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index_old.html", num=number, year=current_year)


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


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    response = requests.get(url=NPOINT_URL)
    response.raise_for_status()
    data = response.json()
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)
