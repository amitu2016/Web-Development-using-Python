from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<marks>")
def home(marks):
    return render_template("index.html", marks = int(marks)) #jinja2 templating


@app.route("/forloop")
def forloop():
    list = [10,20,30,40,50]
    return render_template("forloop.html", marks = list) #jinja2 templating


@app.route("/dictionary")
def dictionary():
    mydict = {"physics" : 50, "Chemistry": 70, "Maths": 60, "Biology": 90}
    return render_template("dict.html", marks=mydict)  # jinja2 templating





@app.route("/contactus")
def contact():
    return render_template("contact.html")


app.run()