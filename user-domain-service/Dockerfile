FROM python:3.7-alpine

COPY . /app
WORKDIR /app
RUN chmod a+x boot.sh

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip3 install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
