"""
Script to initialize WHM App
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


WHM = Flask(__name__)
WHM.config.from_object('config')
DB = SQLAlchemy(WHM)

from src.controllers import sku, order, storage
from src.db import models
