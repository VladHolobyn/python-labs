from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from ..auth.models import User
from . import auth_api_bp


basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.verify_password(password):
        return email
    
@basic_auth.error_handler
def auth_error(status):
    return jsonify(message = "Wrong data! Access denied!") , status

@auth_api_bp.route('/login', methods=['POST'])
@basic_auth.login_required
def login():
    return jsonify(message = "Hello, {}!".format(basic_auth.current_user())) 

# @auth_api_bp.route('/logout', methods=["POST"])
# @login_required
# def logout():
#     pass
