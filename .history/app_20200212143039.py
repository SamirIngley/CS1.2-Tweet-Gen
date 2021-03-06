import sys
sys.path.insert(0, './Code')
from flask import Flask
from Code.stochastic import stoch
from Code.sample import prob_sample
from Code.histogram import list_hist, tuple_hist
from Code.clean_text import clean
app = Flask(__name__)

@app.route('/')
def hello_world():
    num_words=10
    sentence=''
    my_file=('source.txt')
    my_histogram=tuple_hist(my_file)

    for i in range(num_words):
        word = prob_sample(my_histogram)
        sentence += ' ' + word
    return sentence