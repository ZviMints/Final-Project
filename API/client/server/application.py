
from flask import Flask, render_template

app = Flask(__name__)

# Zvi Mints And Eilon Tsadok

@app.route("/graph")
def graph():
    return "graph"
