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
7. Open (http://0.0.0.0:5000/) in browser.

