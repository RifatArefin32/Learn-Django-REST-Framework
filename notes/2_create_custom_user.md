
# Create Custom User
Django has its own `user` class with some possible . But if we want to add some custom fields then we have to create a custom user class. 

**Note that this class has to be created before running our initial migration.** 

## Create an `app` Package
First we will create an `app` packages where all the app modules will reside. 
- First create a directory `apps` from the root directory
- Create an `__init__.py` file which is important to make the dirctory as package

## Create an App `accounts`
Create an app inside the apps package. 
```bash
django-admin startapp accounts
```

After creating the `account` app,
- Update app name with package at `accounts/apps.py` in `package_name.app_name` format. 
- Add the app name in `INSTALLED_APPS` array at `learn_drf/settings.py`.

## Create CustomUser Model
- Create a custom user model `CustomUser`  at `accounts/models.py`
- Add the CustomUser model as default to the `learn_drf/settings.py`. Simply add `AUTH_USER_MODEL = 'accounts.CustomUser'`.

## Run Migration and Start Server
After creating custom user, new we create our first migration file and run migration
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

We can run our server using the following command.
```bash
python3 manage.py runserver
```