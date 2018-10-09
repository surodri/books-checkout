from app import app
from flask import request, Response
import requests
from .decorators import authenticate_user

@app.route('/user/', methods=['POST'])
@authenticate_user
def index():
    
    book = request.args.get('book')

    base_url = app.config['BOOKS_BASE_URL']
    url = f"{base_url}/{book}/checkout"
    response = requests.put(url)
        
    if(response.status_code == requests.codes.ok):
        return Response(book, 200)
    else:
        return Response("Book does not exist" , 404)
