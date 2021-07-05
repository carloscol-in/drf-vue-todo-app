FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./src/server /code
RUN pip install -r requirements/dev.txt
ENTRYPOINT python manage.py runserver 0.0.0.0:8000