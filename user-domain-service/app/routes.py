from app import app
from flask import request, Response

@app.route('/')
@app.route('/user/', methods=['GET'])
def index():
    
    username = request.args.get('username')
    password = request.args.get('password')
    book = request.args.get('book')

    if(password == "s3curePass" and username == "user"):
        return Response(book, 200)
    else:
        return Response(
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})
