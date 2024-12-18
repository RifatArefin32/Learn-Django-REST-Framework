# Project setup

## Create a project directory repo and enter into it
```bash
mkdir LearnDRF
cd LearnDRF
```

## Create a virtual environment for this project and activate it
```bash
python3 -m venv env
source env/bin/activate
```
A virtual environment in Django is crucial because,
- It isolates project dependencies, ensuring that the packages required for one project do not conflict with those of another. 
- By creating a virtual environment, we can install specific versions of libraries and frameworks without affecting the system-wide Python installation or other projects. 
- This isolation makes it easier to manage dependencies, maintain consistency across development and production environments, and collaborate with team members. 

## Install Django and Django REST Framework into the virtual environment
```bash
pip install django
pip install djangorestframework
```

## Create a project and run it
```bash
django-admin startproject mcommerce
cd mcommerce/
python3 manage.py runserver
```

## Register `'rest_framework'` and REST Framework's authentication url
- Add `'rest_framework'` to `INSTALLED_APPS` array of `/mcommerece/settings.py`.
- If we're intending to use the browsable API, we'll probably also want to add REST framework's login and logout views. Add `path('api-auth/', include('rest_framework.urls'))` to `/mcommerece/urls.py` file.


## Setting up `PostgreSQL` database to the project
- Create database and a user for this database. To create a database and a user at PostgreSQL,
```bash
sudo -u postgres psql # enter into postgreSQL cmd
CREATE DATABASE mcommerce_db; # create a database
CREATE USER mcommerce_user WITH PASSWORD 'password'; # create a user for this db
GRANT ALL PRIVILEGES ON DATABASE mcommerce_db TO mcommerce_user; # grant privileges to this user to this db  
```

- Install psycopg2 or psycopg2-binary. `psycopg2` or `psycopg2-binary` are basically PostgreSQL adapter for Python.
```bash
pip install psycopg2
pip install psycopg2-binary # For performance improvements
```

- Add the following items to the `/mcommerece/settings.py` of the project directory
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mcommerce', 
        'USER': 'mcommerce_user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
```

## Run migration from the project directory
```bash
python3 manage.py migrate
```

## Create admin (superuser) for this project
```bash
python3 manage.py createsuperuser
```

## Create `.gitignore` file for the project and initiate git
- Initiate `git` from the project directory repo
- Create a `.gitignore` file for the project
- Push to the `main` branch of github repo


