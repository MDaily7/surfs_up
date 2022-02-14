# import dependencies
from flask import Flask
app = Flask(__name__)
@app.route('/')
def say_hello_world():
    return 'Hello World'





    