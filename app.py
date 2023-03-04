from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

def show_benefits():
    with open("benefits.txt", "r") as f:
        benefits = f.read()
    return benefits
@app.route('/')
def index():
    benefits = show_benefits()
    return f"<html><body><h1>Hello, world!</h1><p>{benefits}</p></body></html>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

