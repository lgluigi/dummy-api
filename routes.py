from flask import Flask, jsonify


app = Flask(__name__)

@app.route("")

def home():
    return jsonify(data="hello from luigi")

def error():
    return jsonify(error="Something really bad happened"), 404