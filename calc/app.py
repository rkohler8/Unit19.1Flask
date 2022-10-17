from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def calc_add():
    """Add a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a,b))

@app.route('/sub')
def calc_sub():
    """Subtract a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a,b))

@app.route('/mult')
def calc_mult():
    """Multiply a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a,b))

@app.route('/div')
def calc_div():
    """Divide a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a,b))

# FURTHER STUDY

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<op>")
def do_math(op):
    """Do specified math operation on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operators[op](a, b))
