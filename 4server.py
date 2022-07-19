# http://localhost:5000/
# http://localhost:5000/read/1
# http://localhost:5000/create
# http://localhost:5000/update/1
# Routing: 이러한 주소와 실제 서비스(index)랑 매핑하는것


from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'

@app.route('/create/')
def create():
    return 'Create'

# @app.route('/read/1/')
# def read():
#     return 'Read 1'

# @app.route('/read/<id>/')
# def read(id):
#     print(id)
#     return 'Read 1'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read '+id

app.run(debug=True)