# coding: utf-8
import json

from flask import Flask, Response, jsonify, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


def getText(filename):
    # Invoke the function using tesseract
    c = {
        "session_id": "0010002",
        "card_number": {
            "value": "5189410064464939",
            "rectangular_box": {
                "left_top": {"x": 200, "y": 200},
                "right_top": {"x": 200, "y": 200},
                "left_bottom": {"x": 200, "y": 200},
                "right_bottom": {"x": 200, "y": 200}
            },
            "confidence": "0.91"
        },
        "expiration": {
            "value": "07/22",
            "rectangular_box": {
                "left_top": {"x": 200, "y": 200},
                "right_top": {"x": 200, "y": 200},
                "left_bottom": {"x": 200, "y": 200},
                "right_bottom": {"x": 200, "y": 200}
            },
            "confidence": "0.91"
        },
        "cardholder_name": {
            "value": "Hanming Li",
            "rectangular_box": {
                "left_top": {"x": 200, "y": 200},
                "right_top": {"x": 200, "y": 200},
                "left_bottom": {"x": 200, "y": 200},
                "right_bottom": {"x": 200, "y": 200}
            },
            "confidence": "0.91"
        }
    }
    json.dump(c, open(filename + ".json", "w"))
    return c


def report(filename, change):
    # Invoke the function using tesseract
    json.dump(change, open(filename + ".json", "w"))


@app.route("/", methods=["GET"])
def hello():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def handler():
    c = request.files["photo"]
    c.save("./" + secure_filename(c.filename))
    return jsonify(getText(c.filename))


if __name__ == '__main__':
    app.run(debug=True)
