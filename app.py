from flask import Flask, request, redirect
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

@app.route("/addtask")
def tasks():
  new_item = {
        "itemname": request.form.get("itemname"),
        "description": request.form.get("description")
    }
  with open("data.json", "r" ) as file:
    data = json.load(file)
    data = []

  data.append(new_item)
  with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True)