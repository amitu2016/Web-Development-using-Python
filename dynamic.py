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


@app.route("/<data>") # dynamic
def contact1(data):
    return "Hello " + data


app.run(port=8081,host='192.168.0.104')  #ip of the machine
