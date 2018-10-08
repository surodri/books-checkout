from app import app
from flask import request, Response
from app.book import Book

@app.route('/<int:id>/checkout', methods=['PUT'])
def checkout(id):

    bookTitle = Book.query.get(id).title

    if(bookTitle):
        return Response("You checked out book id: " + str(id) + " name: " +
        str(bookTitle), 200)
    else:
        return Response("I wish we had that book! Try another", 404)
