from flask import Flask

app = Flask(__name__)

def add (x,y):
    """Add func"""
    return x+y

@app.route("/")
def hello_world():
    x = 1
    y = 2
    return f"<p>x = {x}, y = {y}; add(x,y)={add(x,y)}</p>"