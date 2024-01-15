
class Config:
    DEBUG=True
    TESTING=True
    
    #configuracion  de base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://tu_usuario:tu_contraseña@localhost:3306/tu_basededatos'

class ProductionConfig(Config):
    DEBUG=False
    
class DevelopmentConfig(Config):
    SECRET_KEY='tu_clave_secreta'
    DEBUG=True
    TESTING=True
