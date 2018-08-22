FROM tiangolo/uwsgi-nginx-flask:python2.7

RUN pip install redis

COPY ./app /app

