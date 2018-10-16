from flask import request, Response
from flask import current_app
from app.book import Book
from app import db
from flask import Blueprint

checkout_blueprint = Blueprint('checkout_page', __name__)

def checkout_book(id):

    book = Book.query.get(id)

    if book:
        book_title = book.title
        return Response(f"You checked out book id: {id}, name: {book_title}", 200)
    else:
        return Response("I wish we had that book! Try another", 404)


@checkout_blueprint.route('/<int:id>/checkout', methods=['PUT'])
def checkout(id):

    return checkout_book(id)

@checkout_blueprint.route('/addbook', methods=['POST'])
def add_book():
    new_title = request.json['title']

    new_book = Book( title=new_title)

    db.session.add(new_book)
    db.session.commit()
    books = Book.query.all()

    return Response(str(books), 200) 
