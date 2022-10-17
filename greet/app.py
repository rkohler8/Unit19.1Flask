from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome_msg():
    return "Welcome"

@app.route('/welcome/home')
def welcome_home_msg():
    return "Welcome Home"

@app.route('/welcome/back')
def welcome_back_msg():
    return "Welcome Back"