from flask import Flask
from .extensions import db, migrate, bcrypt, login_manager
from config import config
from app.auth.views import auth
from app.resume.views import resume


def create_app(config_name = 'default'):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        app.register_blueprint(auth, url_prefix='/')
        app.register_blueprint(resume, url_prefix='/resume')
        from app import views
        return app
    