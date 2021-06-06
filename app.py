import json

from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/request")
def req_function():

    name = request.args.get("name") if request.args.get("name") else "null"
    payload = {'name': name}
    res = requests.post("https://knmhttotriggerfunction.azurewebsites.net/api/knmHttpTriggerFunction", data=json.dumps(payload))
    # res = requests.get("https://knmhttotriggerfunction.azurewebsites.net/api/knmHttpTriggerFunction?name=" + name)
    res_txt = res.text

    return res_txt


if __name__ == "__main__":
    app.run(debug=True)
