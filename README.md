
##Run user service 

###Local 
```$ cd user-domain-service
   $ flask run

    Access via 
    http://localhost:5000/user/?username=user&password=s3curePass&book=Linux
```

###Docker container 

```$ docker build -t app_service:latest .

   $ docker  run -it  -p 8000:5000 app_service:latest /bin/sh
```

##Run book service 

``` $ cd book-domain-service
    $ flask run

     Access via
     http://localhost:5000/checkout/?book=Linux
```
