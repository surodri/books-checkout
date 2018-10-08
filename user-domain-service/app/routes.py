from app import app
from flask import request, Response
import requests

@app.route('/')
@app.route('/user/', methods=['GET'])
def index():
    
    username = request.args.get('username')
    password = request.args.get('password')
    book = request.args.get('book')

    if(password == "s3curePass" and username == "user"):
        url = 'http://localhost:5000/' + book + '/checkout'
        response = requests.put(url)
        
        if(response.status_code == requests.codes.ok):
            return Response(book, 200)
        else:
            return Response("Book does not exist" , 404)
    else:
        return Response(
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})
