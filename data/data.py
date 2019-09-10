'''

This script is used to gather data from
reddit API using PRAW and uploads it to MongoDB.

'''

import pymongo
from pymongo import MongoClient
import praw
import pandas as pd
import numpy as np
import os
import datetime as dt

reddit = praw.Reddit(client_id='F8Ny3P98pkrxhA', client_secret='zPYybgK3UTX_xrM10IVyYnb8I68', user_agent='reddit-flair-detector')

flairs = ["AskIndia", "Non-Political", "Reddiquette", "Scheduled", "Photography", "Science/Technology", "Politics", "Business/Finance", "Policy/Economy", "Sports", "Food", "AMA"]

subreddit = reddit.subreddit('india')
data = {"flair":[], "title":[], "body":[], "score":[], "url":[], "num_comm": [], "created": [], "id":[], "author":[], "comm":[]}

for flair in flairs:
  
        posts = subreddit.search(flair, limit = 200)
  
        for post in posts:
        
                data["flair"].append(flair)
                data["title"].append(post.title)
                data["body"].append(post.selftext)
                data["score"].append(post.score)
                data["url"].append(post.url)
                data["num_comm"].append(post.num_comments)
                data["created"].append(post.created)
                data["id"].append(post.id)
                data["author"].append(str(post.author))
                post.comments.replace_more(limit=None)
                comment = ''
                for top_comment in post.comments:
                        comment = comment + ' ' + top_comment.body
                data["comm"].append(comment)

client = MongoClient('mongodb://nitish:umeshpapa123@cluster0-shard-00-00-ifnda.mongodb.net:27017,cluster0-shard-00-01-ifnda.mongodb.net:27017,cluster0-shard-00-02-ifnda.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.database
collection = db.data_collection
posts = db.posts
posts.insert_one(data)

#data = pd.DataFrame(data)
#data.to_json('data.json')
