from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template('index.html')


@app.route("/request")
def request():
    res = requests.get('https://knmhttotriggerfunction.azurewebsites.net/api/knmHttpTriggerFunction', data={'name': 'hello azure'})
    res_txt = res.text

    return res_txt


if __name__ == "__main__":
    app.run(debug=True)
