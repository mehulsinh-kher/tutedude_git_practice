from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def home():
  return "this is the home page please go to (/api) page "


@app.route("/api")
def api():
  with open("data.json") as file:
    data = json.load(file)
    return data


if __name__ == "__main__":
  app.run(debug=True)