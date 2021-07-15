FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./src/server /code

COPY .compose/development/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

RUN pip install -r requirements/test.txt