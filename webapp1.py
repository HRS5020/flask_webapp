from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"

@app.route("/hi/<name>")
def hi_name(name):
    return "Hello %s!" % name


if __name__ == "__main__":
    app.run(debug=True)
