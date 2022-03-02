from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import  Bootstrap5
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap5(app)
moment = Moment(app)
toolbar = DebugToolbarExtension(app)

from sayhello import views, errors, commands
