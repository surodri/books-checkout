from app import app
from flask import request, Response

@app.route('/<int:id>/checkout', methods=['PUT'])
def checkout(id):

    if(id == 1):
        return Response("You checked out book id:" + str(id), 200)
    else:
        return Response("I wish we had that book! Try another", 404)
