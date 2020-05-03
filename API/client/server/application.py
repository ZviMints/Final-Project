
from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

# Zvi Mints And Eilon Tsadok

@app.route("/graph")
def graph():
    return jsonify("this is text that i get from backend")
