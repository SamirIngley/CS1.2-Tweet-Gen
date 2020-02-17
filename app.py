import sys
sys.path.insert(0, './Code')
from flask import Flask, request
from stochastic import stoch
from sample import prob_sample
from histogram import list_hist, tuple_hist
from clean_text import clean
app = Flask(__name__)

@app.route('/')
def sentence_gen():
    num_words = 15
    sentence=''
    my_file=('./Code/source.txt')
    my_histogram=tuple_hist(my_file)

    for i in range(int(num_words)):
        word = prob_sample(my_histogram)
        sentence += ' ' + word
    return sentence


@app.route('/<int:num>')
def sentence_gen_nums(num):
    num_words = 15
    if num:
        num_words=num
    sentence=''
    my_file=('./Code/source.txt')
    my_histogram=tuple_hist(my_file)

    for i in range(int(num_words)):
        word = prob_sample(my_histogram)
        sentence += ' ' + word
    return sentence