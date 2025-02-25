from flask import Flask, render_template
from pprint import pprint
import json

app = Flask(__name__)

data_json = "db_files/data.json"
with open(data_json, 'r') as archive:
    data = json.load(archive)


@app.route("/")
def root():
    return render_template("pages/main.html", data = data)

if __name__ == "__main__":
    app.run(debug=True)