from flask import render_template, request, redirect, url_for, make_response, session
from datetime import datetime
import os
from app import app
import json


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
    if request.method == 'POST':
        username = request.form.get("name")
        password = request.form.get("password")

        json_url = os.path.join(os.path.realpath(os.path.dirname(__file__)), "static/data", "login.json")
        with open(json_url) as f:
            users = json.load(f).get("users")
            if any(user["name"] == username and user["password"] == password for user in users): 
                session["username"] = username
                return redirect(url_for("info_page"))
            else:
                session["error_message"] = "Wrong data! Try again!"
                return redirect(url_for("login"))
    
    if session.get("username"):
        return redirect(url_for("info_page"))   

    return render_template('login.html', message=session.pop("error_message", None), os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())

@app.route('/logout', methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route('/info')
def info_page():
    if not session.get("username"):
        return redirect(url_for("login"))
    return render_template('info.html', username=session.get("username"), os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())