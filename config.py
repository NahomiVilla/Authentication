
class Config:
    DEBUG=True
    TESTING=True
    
    #configuracion  de base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:S251094v@127.0.0.1:3306/mipagina'

class ProductionConfig(Config):
    DEBUG=False
    
class DevelopmentConfig(Config):
    SECRET_KEY='1234'
    DEBUG=True
    TESTING=True