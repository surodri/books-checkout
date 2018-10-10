from app import app
from flask import request, Response
from app.book import Book

@app.route('/<int:id>/checkout', methods=['PUT'])
def checkout(id):

    book = Book.query.get(id)

    if book:
        book_title = book.title
        return Response(f"You checked out book id: {id}, name: {book_title}", 200)
    else:
        return Response("I wish we had that book! Try another", 404)
