from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    res = requests.get('https://knmhttotriggerfunction.azurewebsites.net/api/knmHttpTriggerFunction', data={'name': 'hello azure'})
    return "hello you"
    # return res.text
