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

## Project Setup
- > django-admin startproject firstProject
- > cd firstProject
- > python manage.py startapp firstApp
- Include `'rest_framework'` in `INSTALLED_APPS`
- Create a view
- Create the url
- > python manage.py runserver
- Test with insomnia!

## Level up urls
- Pass urls to app and include in project with `include`.
- Test with insomnia!

## Create first model
- Create a model
- Include model in `INSTALLED_APPS`
- Config settings database connection
- Create database
- > python manage.py makemigrations
- > python manage.py migrate
- Add some data in database
- Refactor view to get data from Model
- Test with insomnia!

## Serializers and function based views
- Create serializer to model
- Refactor view creating model list and model detail views with all HTTP's verb
- Change url's
- Test with insomnia!

## Serializers and Class based views
- Create serializer to model
- Refactor view creating model list and model detail views with all HTTP's verb
- Change url's
- Test with insomnia!

## Serializers and ApiView Class based views
- Create serializer to model
- Refactor view creating model list and model detail views with all HTTP's verb and ApiView
- Change url's
- Test with insomnia!

## Serializers and Generic/mixin Class based views
- Create serializer to model
- Refactor view creating model list and model detail views with all HTTP's verb and Generic/mixin
- Change url's
- Test with insomnia!


