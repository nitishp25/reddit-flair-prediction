# Reddit Flair Predictor

Flask app to predict flair of posts in r/India subreddit. [Click here to launch app.](https://reddit-flair-prediction-pro.herokuapp.com/)

## Codebase

- data: contains python file for collecting data and data.json file
- model: contains model notebook for training models and saving best model
- static: contains css stylesheets
- templates: contains html files for webapp
- Procfile: for heruko
- analysis.py: data analysis of collected data
- app.py: main file for webapp
- final_model1.sav: saved model
- prediction.py: file for predicting flair on given post url
- requirements.txt: contains required dependencies

## Installation

You can either run the app online [here](https://reddit-flair-prediction-pro.herokuapp.com/)

OR

Install it on the machine:
1. `git clone https://github.com/nitishp25/reddit-flair-prediction.git`
2. Create virtual env: `python3 -m venv new-env`
3. Activate this env: `source new-env/bin/activate`
4. `cd reddit-flair-prediction`
5. Install dependencies: `pip install -r requirements.txt`
6. Run `python3 app.py`
7. Open http://0.0.0.0:5000/ in browser.

## Dependencies
- sklearn
- nltk
- PyMongo
- beautifulsoup
- flask
- pandas
- numpy
- praw
- lxml
- scipy
- gunicorn

## Approach

Firstly, all of the data was collected using Praw library which is a python wrapper for Reddit API. The goal was to collect 200 posts of each flair, however, Reddiquette had only around 150 posts.

Secondly, the data was saved on MongoDB using PyMongo.

Thirdly, data was collected from MongoDB and cleaned to remove symbols and bad words using nltk and bs4. The timestamp was created and body, title and comments were cleaned. The comments were not in order so top comments were taken and combined together.

The cleaned data was converted to a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) using Pandas and machine learning models from sklearn were used to train on features like title, body, comments and url to predict flair of a post.

Data was split into training(80%) and testing(20%) set.

The following models were considered for classification:
- Naive Bayes Classifier
- Stochastic Gradient Descent/LinearSVM
- Logistic Regression
- MLP Classifier

The following ensembles were also considered:
- AdaBoost
- Random Forest

The above models were considered due to their robustness and high accuracy and flexibility.

These models were trained on the following features:
- Title
- Body
- Comments
- URL

These features were used because of significant amount of natural language content in them.
Title, comments and URL were combined for multivariate classification to increase accuracy.

Following are the **highest** accuracies for a particular feature:

| Feature               | Model                | Accuracy    |
| --------------------- | -------------------- |:-----------:|
| Title                 | Logistic Regression  | 0.6963      |
| Body                  | SGD/LinearSVM        | 0.3666      |
| URL                   | SGD/LinearSVM        | 0.2972      |
| Comments              | SGD/LinearSVM        | 0.5879      |
| Title, Comments & URL | SGD/LinearSVM        | 0.7440      |

