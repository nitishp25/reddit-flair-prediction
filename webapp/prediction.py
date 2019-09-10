import sklearn
import pickle
import pandas as pd
import praw
import re
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# for cleaning
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):

    text = BeautifulSoup(text, "lxml").text # HTML decoding
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text) # delete symbols which are in BAD_SYMBOLS_RE from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # delete stopwors from text
    return text
    
def tostr(value):
    return str(value)

# to predict flair
def predict(input):
    reddit = praw.Reddit(client_id='F8Ny3P98pkrxhA', client_secret='zPYybgK3UTX_xrM10IVyYnb8I68', user_agent='reddit-flair-detector')

    post = reddit.submission(url=input)
    red = {"title":[], "comm":[], "url":[]}

    # storing the post
    red['title'] = post.title
    post.comments.replace_more(limit=None)
    comment = ''
    for top_comment in post.comments:
        comment = comment + ' ' + top_comment.body
    red["comm"] = comment
    red['url'] = post.url
    
    red['title'] = tostr(red['title'])
    red['title'] = clean_text(red['title'])
    red['comm'] = tostr(red['comm'])
    red['comm'] = clean_text(red['comm'])
    red['url'] = tostr(red['url'])
    
    redd = {"title_comm":[]}

    redd['title_comm'] = red['title'] + red['comm'] + red['url']
    
    #loading model
    model = pickle.load(open('final_model1.sav', 'rb'))
    #prection
    return model.predict([redd['title_comm']])