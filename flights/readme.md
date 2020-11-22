## Instalations
- python 3.8 (default options)
- MySQl web community (server only)
- MySQL workbench community (default options)

## MySQL commands (on workbench)
- show databases;
- create database mydb;
- use mydb;
- show tables;
- select * from firstApp_employee;
- insert into firstApp_employee values(1, 'John', 10000);

## Myvenv Setup
- > python3 -m venv myvenv
- > . myvenv/Scripts/activate
- > pip install django
- > pip install djangorestframework
- > pip install mysqlclient

## Project Flow
- > django-admin startproject nestedSerializers
- > cd nestedSerializers
- > python manage.py startapp fightApp
- Include `'rest_framework'` in `INSTALLED_APPS`
- Include `'fightApp'` in `INSTALLED_APPS`
- Include database configs if database is not Sqlite3
- Create models
- Create serializers
- Create some custom validators on serializers
- Create views (ViewSets, Generics, ApiView, Function based)
- Create urls
- > python manage.py makemigrations
- > python manage.py migrate
- Include `'rest_framework.authtoken'` in `INSTALLED_APPS`
- > python manage.py makemigrations
- > python manage.py migrate
- > python manage.py createsuperuser
- Add IsAuthenticate to some View
- Add api-token-auth route

