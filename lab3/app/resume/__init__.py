from flask import Blueprint

resume_bp = Blueprint('resume', __name__, template_folder='templates', static_folder='static', static_url_path='resume/static')
