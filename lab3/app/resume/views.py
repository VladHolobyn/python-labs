from flask import Blueprint, render_template, request
from datetime import datetime
import os

resume = Blueprint('resume', __name__,url_prefix='/resume', template_folder='templates', static_folder='static', static_url_path='resume/static')


skills = ["java", "postgres", "spring", "hibernate", "junit", "docker"]

@resume.route('/')
@resume.route('/about')
def about_page():
    return render_template('resume/about.html', os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())

@resume.route('/skills')
@resume.route('/skills/<int:id>')
def skills_page(id=None):
    if id is not None and id < len(skills):
        return render_template('resume/skill.html', skill=skills[id])
    else:
        return render_template('resume/skills.html', skills=skills)

@resume.route('/contacts')
def contacts_page():
    return render_template('resume/contacts.html')
