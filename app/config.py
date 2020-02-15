import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'king-k-rool'
    MONGO_URI = os.environ.get('MONGO_URI')
