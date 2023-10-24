from flask import Flask, render_template, request, jsonify
import urllib.request
import json
import os

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route('/api/get-lucky-num', methods=["POST"])
def get_number():
    name = request.json["name"],
    email = request.json["email"],
    year = request.json["year"],
    color = request.json["color"]

    if not color or color.lower() not in ("red", "green", "orange", "blue"):
        error_name = "color"
        error = "Invalid value, must be one of: red, green, orange, blue."
    elif not name:
        error_name = "name"
        error = "This field is required"
    elif not email:
        error_name = "email"
        error = "This field is required"
    elif not year or year < 1900 or year > 2000:
        error_name = "year"
        error = "Invalid year, must be between 1900 and 2000"

    if error_name:
        return jsonify({'errors': {error_name: error}})
        print("**************************", error)
    else:
        url = 'http://numbersapi.com/random/math?write'
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        num = dict["number"]
        num_fact = dict["text"]

        url = f'http://numbersapi.com/${year}/year?json'
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        year_fact = dict["text"]

        return jsonify({'num':
                        {"fact": num_fact,
                         "num": num},
                        "year": {"fact": year_fact,
                                 "year": year}})
