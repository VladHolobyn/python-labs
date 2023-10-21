from flask import Flask


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key="fsCdvb3kb2Dep1gfdkFSD2Fw"

from app import views
