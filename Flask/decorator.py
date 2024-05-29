from time import sleep


def delay_decorator(function):
    print("I am a delay decorator")

    def wrapper_function():
        sleep(3)
        function()

    return wrapper_function


def say_hello():
    sleep(3)
    print("Hello")


def say_greeting():
    print("How are you")


@delay_decorator
def say_bye():
    print("Bye")


say_hello()

decorated_function = delay_decorator(say_greeting)
decorated_function()

say_bye()
