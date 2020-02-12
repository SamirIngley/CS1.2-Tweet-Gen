
from flask import Flask
from stochastic import stoch
from sample import prob_sample
from histogram import list_hist
app = Flask(__name__)

@app.route('/')
def hello_world():
    my_file=open("./words.txt", "r")
    lines=my_file.readlines()
    my_histogram=list_histogram(lines)

    word = prob_sample(my_histogram)

    return word