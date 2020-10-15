How to use it:
--------------

#go to project directory

cd mysite

#create virtual environment

virtualenv env

#activate virtual env

.\env\Scripts\activate

#install dependencies

pip install -r requirements.txt

# Start the application 
python manage.py runserver

# Access the web app in browser: http://127.0.0.1:8000/

a screen will appear with details like

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "employee": "http://127.0.0.1:8000/employee/"
}


Please click the URL to get the employee details




#admin access

after that i have created login
here the route is admin eg: http://127.0.0.1:8000/admin/ 
after clicking in this url you should register sorry for the inconvenience here.

username  = dell
password = Sultan@1234


then you can give post request with the data manager name and employee name

after that if click on get the data will be displayed.
