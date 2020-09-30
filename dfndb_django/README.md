Demonstration Django app starting point.
Steps to create this project:
django-admin startproject dfndb_django  # creates the skeleton file structure for Django
cd dfndb-django 
django-admin startapp dfndb # creates an empty app in the current project

Then to inittialise the app:
python3 ./manage.py migrate # initialises the database (sqlite3 by default)
python3 ./manage.py createsuperuser # makes a username with all priveleges so that you can log into the django-admin

And to run the app on localhost:
python3 ./manage.py runserver
# Then go to http://localhost:8000/admin and log in

There will be few tables defined by default, but we can add those to models.py as per the Django documentation
