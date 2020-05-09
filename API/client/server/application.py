import base64
from io import BytesIO
from flask import jsonify

from flask import Flask, request
from matplotlib.figure import Figure

app = Flask(__name__)

@app.route("/graph", methods = ["POST"])
def graph():
   algorithms = request.get_json().get('algorithms','')
   print("algorithms:" + algorithms)

   # Generate the figure **without using pyplot**.
   fig = Figure()
   ax = fig.subplots()
   ax.plot([1, 2])

   # Save it to a temporary buffer.
   buf = BytesIO()
   fig.savefig(buf, format="png")

   # Embed the result in the html output.
   data = base64.b64encode(buf.getbuffer()).decode("ascii")
   return jsonify(data)

@app.route("/load", methods = ["POST"])
def load():
    return ""

@app.route("/convert", methods = ["POST"])
def convert():
    return ""
