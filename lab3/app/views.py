from flask import render_template, request, redirect, url_for, make_response, session
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

# ?name=&surname  
@app.route('/query') 
def query():
    name = request.args.get("name")
    surname = request.args.get("surname")
    method = request.method
    return f"{name} {surname} {method}"

@app.route('/form', methods=["GET", "POST"]) 
def form():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        isChecked = request.form.get("isChecked")
        return f"{name} {password} {isChecked}"
    else:
        # return redirect(url_for("contacts_page"))
        return render_template('form.html', os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())

@app.route('/set-cookie')
def set_cookie():
    user_name = request.args.get("name")
    if user_name is not None:
        resp = make_response(render_template('cookies.html', name=user_name, os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now()))
        resp.set_cookie("user_name", user_name)
        session["user_name"] = user_name
        return resp
    
    user_name = request.cookies.get("user_name") if request.cookies.get("user_name") else session.get("user_name")

    return render_template('cookies.html', name=user_name, os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())


@app.route('/clear-cookie')
def clear_cookie():
    resp = make_response("Cookies are deleted")
    resp.delete_cookie("user_name")
    # for cookie_key in request.cookies.keys():
        # resp.delete_cookie(cookie_key)
    return resp