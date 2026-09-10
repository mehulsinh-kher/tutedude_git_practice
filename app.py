from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("form.html")


@app.route("/api")
def api():
  with open("data.json") as file:
    data = json.load(file)
    return data


if __name__ == "__main__":
  app.run(debug=True)