from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    html = """
    <h1>Welcome!</h1>"""
    return html

@app.route('/welcome/home')
def welcome_home():
    html = """
    <h1>Welcome home!"""
    return html

@app.route('/welcome/back')
def welcome_back():
    html = """
    <h1>Welcome back!"""
    return html