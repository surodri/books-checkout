
## Run user service 

### Local 
```$ cd user-domain-service
   $ flask run -h localhost -p 8080
```
    Access via 
    http://localhost:8080/user/?username=user&password=s3curePass&book=Linux


### Docker container 

```
   $ docker build -t app_service:latest .

   $ docker  run -it  -p 8080:5000 app_service:latest /bin/sh
```
    Access via
    http://localhost:8080/user/?username=user&password=s3curePass&book=yea

## Run book service 

``` $ cd book-domain-service
    $ flask run
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
