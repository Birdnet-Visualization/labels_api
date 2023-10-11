from flask import Flask
from mongoengine import connect

app = Flask(__name__)

# Configura la conexión a MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'labels',
    'host': 'mongo'  # This matches the service name in docker-compose.yml
}

# Conecta la aplicación a MongoDB
connect(db=app.config['MONGODB_SETTINGS']['db'], host=app.config['MONGODB_SETTINGS']['host'])

from app import routes  # Importa las rutas desde routes.py
