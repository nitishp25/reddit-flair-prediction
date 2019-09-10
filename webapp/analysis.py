'''
This file is used to generate 
visualizations from the collected data
'''

import pandas as pd
import seaborn as sns
import numpy as np
import datetime as dt
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
import pymongo
from pymongo import MongoClient

# getting data from MongoDB
client = MongoClient('mongodb://nitish:umeshpapa123@cluster0-shard-00-00-ifnda.mongodb.net:27017,cluster0-shard-00-01-ifnda.mongodb.net:27017,cluster0-shard-00-02-ifnda.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.database
collection = db.data_collection
posts = db.posts
data = posts.find_one()

data = pd.DataFrame(data)
flairs = ["AskIndia", "Non-Political", "Reddiquette", "Scheduled", "Photography", "Science/Technology", "Politics", "Business/Finance", "Policy/Economy", "Sports", "Food", "AMA"]
comments = []
scr = []

# counting upvotes and no of comments
for fl in flairs:
    comm = 0
    s = 0
    for index, row in data.iterrows():
        if(row.flair == fl):
            comm += row.num_comm
            s += row.score
    comments.append(comm)
    scr.append(s)

df = pd.DataFrame(list(zip(flairs, scr, comments)), columns =['Flair', 'Score', 'Comments'])
df1 = ColumnDataSource(df) 

# flair vs upvotes
fig1 = figure(title='Flair vs Upvotes',
             plot_height=400, plot_width=1500, x_range = flairs,
             x_axis_label='Flair', y_axis_label='Upvotes')

fig1.vbar(x='Flair', top='Score', source=df1, color='blue', width=0.5, legend='Upvotes')

# flair vs comments
fig2 = figure(title='Flair vs Comments',
             plot_height=400, plot_width=1500, x_range = flairs,
             x_axis_label='Flair', y_axis_label='No. of comments')

fig2.vbar(x='Flair', top='Comments', source=df1, color='red', width=0.5, legend='Comment')

fig1.legend.location = 'top_left'
fig2.legend.location = 'top_left'

# hover tools
tooltip1 = [('Upvotes', '@Score'), ('Flair', '@Flair')]
fig1.add_tools(HoverTool(tooltips=tooltip1))

tooltip2 = [('Comment', '@Comments'), ('Flair', '@Flair')]
fig2.add_tools(HoverTool(tooltips=tooltip2))

panel1 = Panel(child=fig1, title='Flair vs Upvotes')
panel2 = Panel(child=fig2, title='Flair vs Comments')

# flair vs time
def todate(created):
    return dt.datetime.fromtimestamp(created)
    
created = data["created"].apply(todate)
data = data.assign(created = created)

time = []

for index, row in data.iterrows():
    time.append(int(row.created.hour))

data['time'] = time

tabs = Tabs(tabs=[panel1, panel2])

sns.set_style("whitegrid")

# output couldn't be rendered on html so saved an image
ax = sns.violinplot(x="flair", y="time", data=data, width=0.5)
ax.figure.savefig("time.png")

show(tabs)

output_file('analysis.html', title='Data Analysis')