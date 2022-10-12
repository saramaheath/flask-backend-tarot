import os
from dotenv import load_dotenv
import json

from flask import Flask, jsonify, request, render_template, redirect
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Card, Deck

load_dotenv()

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
#toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()