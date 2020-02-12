
from flask import Flask
from stochastic import stoch
from sample import prob_sample
from histogram import list_hist
from clean_text import clean
app = Flask(__name__)

@app.route('/')
def hello_world():

    my_file=open("./words.txt", "r")
    my_histogram=list_hist(my_file)
    word = prob_sample(my_histogram)

    return word