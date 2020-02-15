from flask import Flask
from app.config import Config
from flask_pymongo import PyMongo
import dns
mongo = PyMongo()
app = Flask(__name__)
app.config.from_object(Config)
mongo.init_app(app)
from app import routes
