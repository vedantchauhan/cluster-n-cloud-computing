from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import datetime
from couchdbkit import Document, StringProperty, DateTimeProperty
import couchdbkit
import json


# configuration
from flask.json import jsonify

DATABASE = 'aurin'
DATABASE_TWEETS = 'tweets'
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'admin'
url = 'http://admin:admin@172.17.0.3:5984'

# create our application
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#variables
count_pos_melb = 0
count_neg_melb = 0
melb_score = 0
count_pos_syd = 0
count_neg_syd = 0
syd_score = 0
count_pos_dar = 0
count_neg_dar = 0
dar_score = 0
count_pos_per = 0
count_neg_per = 0
per_score = 0
count_pos_ade = 0
count_neg_ade = 0
ade_score = 0
count_pos_bri = 0
count_neg_bri = 0
bri_score = 0
count_pos_hob = 0
count_neg_hob = 0
hob_score = 0
count_pos_can = 0
count_neg_can = 0
can_score = 0


# connecting to couchdb
def connect_db():
    server = couchdbkit.Server()
    return server.get_or_create_db(app.config['DATABASE'])

def connect_db_tweets():
    server = couchdbkit.Server()
    return server.get_or_create_db(app.config['DATABASE_TWEETS'])

def tweets():
    try:
        db_tweets = connect_db_tweets()
        for item in db_tweets.view('group49/melb_pos', include_docs=True):
            count_pos_melb = item["rows"]["value"]
        for item in db_tweets.view('group49/melb_neg', include_docs=True):
            count_neg_melb = item["rows"]["value"]
        melb_score = count_pos_melb / count_neg_melb

        for item in db_tweets.view('group49/syd_pos', include_docs=True):
            count_pos_syd = item["rows"]["value"]
        for item in db_tweets.view('group49/syd_neg', include_docs=True):
            count_neg_syd = item["rows"]["value"]
        syd_score = count_pos_syd / count_neg_syd

        for item in db_tweets.view('group49/bri_pos', include_docs=True):
            count_pos_bri = item["rows"]["value"]
        for item in db_tweets.view('group49/bri_neg', include_docs=True):
            count_neg_bri = item["rows"]["value"]
        bri_score = count_pos_bri / count_neg_bri

        for item in db_tweets.view('group49/can_pos', include_docs=True):
            count_pos_can = item["rows"]["value"]
        for item in db_tweets.view('group49/can_neg', include_docs=True):
            count_neg_can = item["rows"]["value"]
        can_score = count_pos_can / count_neg_can

        for item in db_tweets.view('group49/ade_pos', include_docs=True):
            count_pos_ade = item["rows"]["value"]
        for item in db_tweets.view('group49/ade_neg', include_docs=True):
            count_neg_ade = item["rows"]["value"]
        ade_score = count_pos_ade / count_neg_ade

        for item in db_tweets.view('group49/hob_pos', include_docs=True):
            count_pos_hob = item["rows"]["value"]
        for item in db_tweets.view('group49/hob_neg', include_docs=True):
            count_neg_hob = item["rows"]["value"]
        hob_score = count_pos_hob / count_neg_hob

        for item in db_tweets.view('group49/per_pos', include_docs=True):
            count_pos_per = item["rows"]["value"]
        for item in db_tweets.view('group49/per_neg', include_docs=True):
            count_neg_per = item["rows"]["value"]
        per_score = count_pos_per / count_neg_per

        for item in db_tweets.view('group49/dar_pos', include_docs=True):
            count_pos_dar = item["rows"]["value"]
        for item in db_tweets.view('group49/dar_neg', include_docs=True):
            count_neg_dar = item["rows"]["value"]
        dar_score = count_pos_dar / count_neg_dar

    except Exception as e:
        print(e)


@app.route('/',methods=['GET','POST'])
def show_entries():
    db = connect_db()
    rows = db.view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    #df = pd.DataFrame(data)
    response = {}
    for d in data:
        response.update({d['city']: d['median_income']})
    return render_template('show_entries.html', response=response)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/analysis_one')
def analysis_one():
    return render_template('analysis_one.html')

@app.route('/analysis_two')
def analysis_two():
    return render_template('analysis_two.html')

@app.route('/analysis_three')
def analysis_three():
    return render_template('analysis_three.html')

if __name__ == '__main__':
    app.run()
