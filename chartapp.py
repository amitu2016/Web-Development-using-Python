from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def chart():
    labels = ["jan","feb","march","april","may","june","july","aug"]
    values = [10,9,7,8,6,9,5,2]
    return render_template('chart.html',values=values,labels=labels)


if __name__ == "__main__":
    app.run()