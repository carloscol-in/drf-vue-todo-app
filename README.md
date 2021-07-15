# Todo Application

> This is a Todo application that you can clone and use in your company to manage the tasks; creation, reading, deleting and updating. It is meant to improve collaboration throughout organizations and its teams, as well as tracking productivity and execution of tasks to meet goals and deadlines.

This app will be using Vue.js on the Frontend and Django REST Framework on the backend. The app by default will use a PostgreSQL database that is configured in the `compose` files. If you want to use another source, you could override some environment variables set on each of the `compose` files. Below on the document will be detailed how to do that.

## How to run

> This applications uses `docker compose`, if you don't have it installed yet, visit the [Docker's official](https://docs.docker.com/compose/install/) documentation on how to install it.

This application has two environments; development, testing and production. Production compose file should be named in a way that makes it easy to docker-compose to run; `docker-compose.yml`. 

The development environment has debugging tools such as `django-extensions`. If you want to call for example the `shell_plus` that `django-extensions` provides, then all you have to do, supposing you already built the `docker-compose` file, is run this command:

```
docker-compose -f development.yml run --rm django python manage.py shell_plus
```

## Testing

The app already has a `docker-compose` file for testing only, which you can build and run.
