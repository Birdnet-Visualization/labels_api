from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from mongoengine import connect

app = Flask(__name__)
CORS(app)
app.config['MONGODB_SETTINGS'] = {
    'db': 'labels',
    'host': 'mongodb://root:vitocox18@mongo:27017/labels'
}

connect(db=app.config['MONGODB_SETTINGS']['db'], host=app.config['MONGODB_SETTINGS']['host'])

from app import routes  # Importa las rutas desde routes.py
