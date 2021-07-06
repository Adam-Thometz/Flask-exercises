from operations import *
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def do_add():
    """Add a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a, b))

@app.route('/sub')
def do_subtract():
    """Subtract b from a"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a, b))

@app.route('/mult')
def do_mult():
    """Multiply a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a, b))

@app.route('/div')
def do_div():
    """Divide a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a, b))

# Alt

OPERATIONS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<op>')
def do_math(op):
    """Do an operaton on a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(OPERATIONS[op](a, b))