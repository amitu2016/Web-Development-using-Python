from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello I am Home Page"


@app.route("/contact")
def contact():
    return "Hello I am contact page"


@app.route("/aboutus")
def aboutus():
    return "Hello I am abutus Page"


app.run()
