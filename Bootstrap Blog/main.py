import requests
from flask import Flask, render_template

NPOINT_URL = "https://api.npoint.io/77df45bbba34b98349f4"

app = Flask(__name__)

response = requests.get(NPOINT_URL)
response.raise_for_status()
data = response.json()


@app.route("/")
def home():
    return render_template("index.html", blog_posts=data)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:pid>")
def post(pid):
    return render_template("post.html", post=data[pid - 1])


if __name__ == "__main__":
    app.run(debug=True)
