## Tech stack 

    - python 3.7
    - pipenv 
    - flask
    - sqlalchemy
    - flask-migrate
    - pytest
    - Docker

## User service

Add flask variable. By default flask will look for app.py

``` $ cd user-domain-service
    $ export FLASK_APP=app_service.py
```

# run locally
```
    $ pipenv run flask run -h localhost -p 8080
```
    Access via
```
    $curl -X POST \
    'http://localhost:8080/user/?book=1' \
    -H 'content-type: application/json' \
    -d '{
	    "username": "user",
	    "password": "s3curePass"
    }'
```
http://localhost:8080/user/?username=user&password=s3curePass&book=Linux


### Docker container 

```
   $ docker build -t app_service:latest .

   $ docker  run -it  -p 8080:5000 app_service:latest /bin/sh
```
    Access via
    http://localhost:8080/user/?username=user&password=s3curePass&book=yea

## Book service 

# Setup

``` 
    $ cd book-domain-service
```

Add flask variable. By default flask will look for app.py
```
    $ export FLASK_APP=app_service.py
```

# Set up database 

Initialize database and migratios folder
```
    $  pipenv run flask db init
```
Create the first database migration. 
Note: -m adds descriptive text "" to the migration file name
```
    $ pipenv run flask db migrate -m "book"
```
Apply migration to the database
```
    $ pipenv run flask db upgrade
```

Reference: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database/page/2

### Run locally
```
    $ pipenv run flask run
```
     Access via
     http://localhost:5000/<book id>/checkout

### Docker container

```
    $ docker build -t app_service:latest .
    
    $ docker  run -it  -p 8080:5000 app_service:latest /bin/sh
```
    Access via
    http://localhost:8080/<book id>/checkout
