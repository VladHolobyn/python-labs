from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())

@app.route('/skills')
def skills():
    os.
    return render_template('skills.html', os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', os=os.name, user_agent=request.headers.get('User-Agent'), time=datetime.now())


if __name__ == '__main__':
    app.run()