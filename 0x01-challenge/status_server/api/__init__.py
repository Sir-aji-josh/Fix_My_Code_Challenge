#!/usr/bin/python3
""" 
Views module
"""
import sys
from flask import Flask

app = Flask(__name__)

from api.v1.views import app_views
app.register_blueprint(app_views)

from api.v1.views.index import *

