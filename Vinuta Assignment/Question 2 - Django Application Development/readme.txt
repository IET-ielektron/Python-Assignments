Create a virtual environment (optional)
python version used: 3.6
Django version used: 3.1.2
Libraries to be installed: django, django_rest_framework

Django project name: django_rest 
Application name: employee

Steps:
1) You can create virtual environment and add the django project or can directly run the project.
2) Install above mentioned libraries.
3) Run below migration commands to create default django tables and models:if needed
python manage.py makemigrations
python manage.py migrate
4) Command to run project: go to project path and run - python manage.py runserver
5) open the application in browser with following url
localhost:8000/employees
