
from flask import Flask
from stochastic import stoch
app = Flask(__name__)

@app.route('/')
def hello_world():
    return stoch()