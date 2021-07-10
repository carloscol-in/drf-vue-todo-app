# Todo Application

> This is a Todo application that you can clone and use in your company to manage the tasks; creation, reading, deleting and updating. It is supposed to improve collaboration throughout organizations and its teams.

## How to run

> This applications uses `docker compose`, if you don't have it installed yet, visit the [Docker's official](https://docs.docker.com/compose/install/) documentation on how to install it.

This application has two environments; development, testing and production. Production compose file should be named in a way that makes it easy to docker-compose to run; `docker-compose.yml`. 

The development environment has debugging tools such as `django-extensions`. If you want to call for example the `shell_plus` that `django-extensions` provides, then all you have to do, supposing you already built the `docker-compose` file, is run this command:

```
docker-compose -f development.yml run --rm django python manage.py shell_plus
```

## Testing

The app already has a `docker-compose` file for testing only, which you can build and run.
