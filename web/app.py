from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import datetime
from couchdbkit import Document, StringProperty, DateTimeProperty
import couchdbkit


# configuration
DATABASE = 'web'
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

