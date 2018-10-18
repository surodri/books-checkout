from flask import request, Response, jsonify, Blueprint
from sqlalchemy import exc
from .book import Book
from app import db

checkout_blueprint = Blueprint('checkout_page', __name__)

@checkout_blueprint.route('/<int:id>/checkout', methods=['PUT'])
def checkout(id):

    book = Book.query.get(id)

    if book:
        book_title = book.title
        return Response(f'You checked out book id: {id}, name: {book_title}', 200)
    else:
        return Response('I wish we had that book! Try another', 404)

@checkout_blueprint.route('/addbook', methods=['POST'])
def add_book():
    new_title = request.json.get('title')

    new_book = Book.from_json(request.json)
    try:
        db.session.add(new_book)
        db.session.commit()
        db.session.flush()

    except exc.IntegrityError:
        db.session.rollback()
        return Response('This book already exists! Titles must be unique', 400)

    return jsonify(new_book.to_json()), 200
