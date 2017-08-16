from jinja2 import StrictUndefined
from flask import (Flask, render_template, redirect, request, flash,
                    session, jsonify, url_for)

# from flask_debugtoolbar import DebugToolbarExtension

from model import Player, RSGame, PLGame
from model import connect_to_db, db

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar


app.jinja_env.undefined = StrictUndefined