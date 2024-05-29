from flask import Flask

app = Flask(__name__)


# print(__name__)
def make_bold(function):
    def wrapper_function():
        string = function()
        return f"<b>{string}</b>"

    return wrapper_function


def make_italic(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        string = function()
        return "<u>" + string + "</u>"

    return wrapper_function


@app.route("/")
def hello_world():
    # return "Hello, World!"
    return ('<h1 style="text-align: center">Hello</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXIweGVrMG9hdm5hNGEwcnE2OGxqMGRkeWI2cTg1NmQ2N3l2OTc3aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/utz68KlKM5LGBVF6HZ/giphy.gif" alt="Rocket" width=200>')


@app.route("/bye")
@make_bold
@make_italic
@make_underlined
def bye():
    # return "<u><em><b>Bye!</b></em></u>"
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello, {name} and number is {number}!"


if __name__ == "__main__":
    app.run(debug=True)
