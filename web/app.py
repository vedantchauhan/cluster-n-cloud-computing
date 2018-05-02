from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import datetime
from couchdbkit import Document, StringProperty, DateTimeProperty
import couchdbkit
import pandas as pd


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

@app.route('/show_entries', methods=['GET','POST'])
def show_entries():
    db = connect_db()
    rows = db.view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    df = pd.DataFrame(data)
    response = {
        "city": df['city'],
        "median_age": df['median_age']
    }
    return render_template('show_entries.html', test=response)

'''@app.route('/', methods=['GET','POST'])
def show_entries():
    db = connect_db()
    rows = db.view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    df = pd.DataFrame(data)
    response = {
        "city": df['city'],
        "median_age": df['median_age']
    }
    city = ["Melbourne", "Sydney"]
    return render_template('show_entries.html', **locals())'''

if __name__ == '__main__':
    app.run()
