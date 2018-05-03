from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import datetime
from couchdbkit import Document, StringProperty, DateTimeProperty
import couchdbkit
import pandas as pd
import json


# configuration
from flask.json import jsonify

DATABASE = 'aurin'
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'admin'

# create our application
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# connectin to couchdb
def connect_db():
    server = couchdbkit.Server()
    return server.get_or_create_db(app.config['DATABASE'])


@app.route('/',methods=['GET','POST'])
def show_entries():
    db = connect_db()
    rows = db.view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    #df = pd.DataFrame(data)
    response = {}
    for d in data:
        response.update({d['city']: d['median_age']})
    return render_template('show_entries.html', response=response)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/analysis_one')
def analysis_one():
    return render_template('analysis_one.html')

@app.route('/analysis_two')
def analysis_one():
    return render_template('analysis_two.html')

@app.route('/analysis_three')
def analysis_one():
    return render_template('analysis_three.html')

if __name__ == '__main__':
    app.run()
