class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def decorator_function(function):
    def wrapper_function(*args, **kwargs):
        args[0].is_logged_in = True
        function(args[0])

    return wrapper_function


@decorator_function
def check_login_status(user):
    if user.is_logged_in:
        print("Login status is True")


user = User("Saqib")
check_login_status(user)

# Let's add a decorator to set the login status True before user checks login status
