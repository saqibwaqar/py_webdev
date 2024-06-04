from flask import Flask, render_template
import requests
from post import Post

NPOINT_URL = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

response = requests.get(NPOINT_URL)
response.raise_for_status()
data = response.json()


@app.route('/')
def home():
    return render_template("index_old.html", blog_posts=data)


@app.route("/post/<int:pid>")
def get_post(pid):
    # Find the dict in list with desired id
    post = None
    for item in data:
        if item["id"] == pid:
            post = Post(item["title"], item["subtitle"], item["body"])
            break

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
