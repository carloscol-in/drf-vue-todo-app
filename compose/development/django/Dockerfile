FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./src/server /code
RUN pip install -r requirements/dev.txt
RUN python manage.py makemigrations &&\
    python manage.py migrate