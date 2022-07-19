from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    # return 'hello'
    # return str(random.random())
    return 'random : <strong>'+str(random.random())+'</strong>'

app.run(debug=True)