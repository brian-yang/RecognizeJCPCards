# coding: utf-8
import json
import numpy as np
import base64

from flask import Flask, Response, jsonify, request, render_template
from werkzeug.utils import secure_filename
from jcpcv import GetInformation
import cv2

app = Flask(__name__)

def report(filename, change):
    # Invoke the function using tesseract
    json.dump(change, open(filename + ".json", "w"))


@app.route("/", methods=["GET"])
def hello():
    return render_template("index.html")

def decode_base64(string):
    data = string.split(",")[1]
    data = base64.b64decode(data)
    nparr = np.fromstring(data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


@app.route("/", methods=["POST"])
def handler():
    c = request.form["photo"]
    s = decode_base64(c)
    cv2.imwrite("1.jpg", s)
    return jsonify(GetInformation(cv2.imread("1.jpg", 0)))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
