from flask import Flask
from mongoengine import connect

app = Flask(__name__)

# Configura la conexión a MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'labels',  # Nombre de la base de datos
    'host': 'mongodb://mongo:27017/labels'  # URI de conexión de MongoDB
}

# Conecta la aplicación a MongoDB
connect(db=app.config['MONGODB_SETTINGS']['db'], host=app.config['MONGODB_SETTINGS']['host'])

from app import routes  # Importa las rutas desde routes.py