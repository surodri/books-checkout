FROM python:3.7-alpine

COPY app app
COPY app_service.py ./
COPY boot.sh ./
RUN chmod a+x boot.sh

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip3 install gunicorn

# -- Install Pipenv:

RUN pip3 install pipenv

# -- Install dependencies:
RUN pipenv install 

ENV FLASK_APP app_service.py

EXPOSE 5000
CMD ["./boot.sh"]
