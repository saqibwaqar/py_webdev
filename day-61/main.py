from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.simple import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), validators.Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "some secret string"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
