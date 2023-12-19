from flask import jsonify
from marshmallow import ValidationError
from . import user_api_bp

@user_api_bp.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400
