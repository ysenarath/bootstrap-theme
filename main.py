from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cheatsheet")
def cheatsheet():
    return render_template("cheatsheet.html")


if __name__ == "__main__":
    app.run(debug=True, port=5066)
