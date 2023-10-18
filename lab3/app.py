from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run()