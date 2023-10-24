from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route('/api/get-lucky-num', methods=["POST"])
def get_number():
    name = request.json["name"]
    email = request.json["email"]
    year = request.json["year"]
    color = request.json["color"]
    errors = {}

    if not color or color.lower() not in ("red", "green", "orange", "blue"):
        errors["color"] = "Invalid value, must be one of: red, green, orange, blue."
    if not name:
        errors["name"] = "This field is required"
    if not email:
        errors["email"] = "This field is required"
    if not year or int(year) < 1900 or int(year) > 2000:
        errors["year"] = "Invalid year, must be between 1900 and 2000"

    if errors:
        return jsonify({'errors': errors})

    else:
        r = requests.get('http://numbersapi.com/random/trivia?json')
        data = r.json()
        num = data["number"]
        num_fact = data["text"]

        res = requests.get(f'http://numbersapi.com/1909/year?json')
        data = res.json()
        year_fact = data["text"]
        return jsonify({'num':
                        {"fact": num_fact,
                         "num": num},
                        "year": {"fact": year_fact,
                                 "year": 1909}})
