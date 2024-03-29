from flask import Flask
from .extensions import db, migrate, bcrypt, login_manager, jwt_manager, ma, admin
from config import config
from app.admin_panel.views import SecuredIndexView, UserAdminView, SecuredFileAdmin
from app.auth.models import User
from app.auth.views import auth_bp
from app.auth_api.views import auth_api_bp
from app.resume.views import resume_bp
from app.cookies.views import cookies_bp
from app.todo.views import todo_bp
from app.todo_api.views import todo_api_bp
from app.feedbacks.views import feedbacks_bp
from app.posts.views import posts_bp
from app.user_api import user_api_bp
from app.swagger import swagger_bp


def create_app(config_name = 'default'):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)
    jwt_manager.init_app(app)

    admin.init_app(app, index_view=SecuredIndexView())
    admin.add_view(UserAdminView(User, db.session))
    admin.add_view(SecuredFileAdmin(app.static_folder, '/static/', name='Static Files'))

    with app.app_context():
        app.register_blueprint(auth_bp, url_prefix='/')
        app.register_blueprint(resume_bp, url_prefix='/resume')
        app.register_blueprint(cookies_bp, url_prefix='/cookies')
        app.register_blueprint(todo_bp, url_prefix='/todo')
        app.register_blueprint(feedbacks_bp, url_prefix='/feedbacks')
        app.register_blueprint(posts_bp, url_prefix='/posts')
        app.register_blueprint(todo_api_bp, url_prefix='/api/todos')
        app.register_blueprint(auth_api_bp, url_prefix='/api/auth')
        app.register_blueprint(user_api_bp, url_prefix='/api')
        app.register_blueprint(swagger_bp, url_prefix='/swagger')
        return app
    