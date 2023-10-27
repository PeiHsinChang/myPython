''' 
1. 安裝 Flask 框架
- pip install Flask
'''
import requests

from flask import Flask
app = Flask(__name__)





# >>>> Response<200>

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/test')
def test():
    return "This is a test page"

@app.route('/test11')
def test11():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response)
    print(response.json())
    return response.json()
app.debug = True