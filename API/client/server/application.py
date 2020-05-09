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
    # json

@app.route("/convert", methods = ["POST"])
def convert():
    # param withConnected = true / false
    # input: JSON
    # output: png


# getKMeans(json) (can get only train or test)
    # (f1) convert to node2vec (json) -> (networkx) -> .. node2vec .. -> (node64)
    # (f2) PCA(vec64) -> vec3
    # (f3) Result -> show Result


# getKmeans(string) - this string can be train or test
    # load(string) ->
        # def load(string)
            # if(string == "train")
                # return ./server/train.json
            # else
