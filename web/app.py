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


def init_db():
    """Creates the database views."""
    db = connect_db()
    loader = couchdbkit.loaders.FileSystemDocsLoader('_design')
    loader.sync(db, verbose=True)


class Entry(Document):
    author = StringProperty()
    date = DateTimeProperty()
    title = StringProperty()
    text = StringProperty()



@app.before_request
def before_request():
    """Make sure we are connected to the database each request."""
    g.db = connect_db()
    Entry.set_db(g.db)

@app.route('/')
def show_entries():
    # ? entries = Entry.view('entry/all')
    entries = g.db.view('entry/all', schema=Entry)
    #app.logger.debug(entries.all())
    return render_template('show_entries.html', entries=entries)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run()
