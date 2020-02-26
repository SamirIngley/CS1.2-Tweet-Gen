import sys
import os
sys.path.insert(0, './Code')
from flask import Flask, request
from stochastic import stoch
from sample import prob_sample
from histogram import list_hist, tuple_hist
from clean_text import clean
from markov_chain import Markov
from twee import Tweeter
app = Flask(__name__)



consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

tweeter = Tweeter(consumer_key, consumer_secret, access_token, access_token_secret)

@app.route('/')
def sentence_gen():
    markov = Markov('./Code/source.txt')
    sentence = markov.random_walk(13)
    tweeter.send(sentence)
    return sentence


@app.route('/<int:num>')
def sentence_gen_nums(num):
    markov = Markov('./Code/source.txt')
    sentence = markov.random_walk(num)
    tweeter.send(sentence)
    return sentence