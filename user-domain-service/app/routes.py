from app import app
from flask import request

@app.route('/')
@app.route('/index/', methods=['GET'])
def index():

    book = request.args.get('book')
    
    return book
