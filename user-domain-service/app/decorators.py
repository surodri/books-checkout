from flask import request, Response

def authenticate_user (func):
    def wrapper_authenticate(*args, **kwargs):

        username = request.args.get('username')
        password = request.args.get('password')
        

        if(password == "s3curePass" and username == "user"):
            return func(*args, **kwards)
        else: 
            return Response(
            'You have to login with proper credentials', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'})
            
    return wrapper_authenticate
