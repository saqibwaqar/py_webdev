import smtplib
from email.message import EmailMessage
import requests, os
from flask import Flask, render_template, request

NPOINT_URL = "https://api.npoint.io/77df45bbba34b98349f4"

SOURCE_EMAIL = os.environ.get("SOURCE_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
DEST_EMAIL = os.environ.get("DEST_EMAIL")

app = Flask(__name__)

response = requests.get(NPOINT_URL)
response.raise_for_status()
data = response.json()


def send_email(name, email, phone, message):
    email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        msg = EmailMessage()
        msg.set_content(email_message)
        msg['subject'] = "New Message"
        msg['to'] = DEST_EMAIL
        msg['from'] = SOURCE_EMAIL
        connection.starttls()
        connection.login(user=SOURCE_EMAIL,
                         password=MY_PASSWORD)
        connection.send_message(msg)


@app.route("/")
def home():
    return render_template("index.html", blog_posts=data)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        success_message = "Successfully sent your message"

        send_email(name, email, phone, message)

        return render_template("contact.html", success_message=True)
    return render_template("contact.html", success_message=False)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    print(request.form["name"])
    print(request.form["email"])
    print(request.form["phone"])
    print(request.form["message"])

    return "<h1>Successfully sent your message</h1>"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:pid>")
def post(pid):
    clicked_post = None
    for item in data:
        if item["id"] == pid:
            clicked_post = item

    return render_template("post.html", post=clicked_post)


if __name__ == "__main__":
    app.run(debug=True)
