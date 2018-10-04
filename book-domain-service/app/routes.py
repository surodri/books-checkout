from app import app
from flask import request, Response

@app.route('/')
@app.route('/checkout/', methods=['GET'])
def index():

    book = request.args.get('book')

    if(book == "Linux"):
        return Response("You checked out :" + book, 200)
    else:
        return ("I wish we had that book! Try another", 401)
