from datetime import timedelta
import os


basedir = os.path.abspath(os.path.dirname(__file__))

ACCESS_EXPIRES = {
    'access': timedelta(hours=1),
    'refresh': timedelta(days=1)
}

class Config(object):
    WTF_CSRF_ENABLED = True
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    SECRET_KEY = 'secret'
    JWT_SECRET_KEY = "super-secret" 
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES['access']
    JWT_REFRESH_TOKEN_EXPIRES = ACCESS_EXPIRES['refresh']
    FLASK_SECRET = SECRET_KEY

class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "instance\\site.sqlite")
    REDIS_DB_URI = 'redis://localhost:6379'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('FLASK_DB_URL')
    REDIS_DB_URI = os.environ.get('REDIS_DB_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    FLASK_SECRET = SECRET_KEY

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "instance\\test-db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SERVER_NAME = '127.0.0.1:5000'

    
config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig,
    'test': TestConfig
}
