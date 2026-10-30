import datetime

def get_date():
    today = datetime.datetime.now()
    return today.strftime("%Y-%m-%d")

def say_hello(name):
    return "Hello " + name

def check_input(text):

    if text == "":
        return False

    return True

def make_id():
    return str(datetime.datetime.now().timestamp())
