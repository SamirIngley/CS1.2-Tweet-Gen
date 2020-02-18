import sys
sys.path.insert(0, './Code')
from flask import Flask, request
from stochastic import stoch
from sample import prob_sample
from histogram import list_hist, tuple_hist
from clean_text import clean
from markov_chain import Markov
app = Flask(__name__)

@app.route('/')
def sentence_gen():
    markov = Markov('./Code/source.txt')
    return markov.random_walk(20)


@app.route('/<int:num>')
def sentence_gen_nums(num):
    markov = Markov('./Code/source.txt')
    return markov.random_walk(num)