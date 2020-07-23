from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello I am Home Page"


@app.route("/<name>/<marks>")
def calculate(name,marks):
    if int(marks) < 50:
        result = "fail"
    else:
        result = "Pass"

    return "Hello " + name + " Your marks is " + marks + " and you are " + result


app.run()