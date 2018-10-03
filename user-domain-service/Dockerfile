FROM python:3.7-alpine

RUN adduser -D app_service

WORKDIR /home/app_service

# -- Install Pipenv:
RUN apk update && apk upgrade && apk install python3.7-dev 
RUN curl --silent https://bootstrap.pypa.io/get-pip.py | python3.7

# Backwards compatility.
RUN rm -fr /usr/bin/python3 && ln /usr/bin/python3.7 /usr/bin/python3

RUN pip3 install pipenv

RUN pipenv install
RUN pipenv install gunicorn --dev

COPY app app
COPY app_service.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP app_service.py

RUN chown -R app_service:app_service ./
USER app_service

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
