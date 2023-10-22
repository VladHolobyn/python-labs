from flask import render_template, request
from datetime import datetime
import os
from app import app


skills = ["java", "postgres", "spring", "hibernate", "junit", "docker"]

@app.route('/')
@app.route('/about')
def about_page():
    return render_template('about.html', os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())

@app.route('/skills')
@app.route('/skills/<int:id>')
def skills_page(id=None):
    if id is not None and id < len(skills):
        return render_template('skill.html', skill=skills[id], os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())
    else:
        return render_template('skills.html', skills=skills, os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())

@app.route('/contacts')
def contacts_page():
    return render_template('contacts.html', os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())

@app.route('/info')
def info_page():
    return render_template('info.html', os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())