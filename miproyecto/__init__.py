from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)

#cargar las configuraciones
app.config.from_object('config.DevelopmentConfig')
db=SQLAlchemy(app)
#importar vistas
from miproyecto.views.auth import auth 
app.register_blueprint(auth)

db.create_all