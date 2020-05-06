Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Thanks for checking it out.

To contribute to Django:

Check out https://docs.djangoproject.com/en/dev/internals/contributing/ for information about getting involved.


Requirements

Python -
(3.5, 3.6, 3.7, 3.8)


Django -
(2.2, 3.0)
We highly recommend and only officially support the latest patch release of each Python and Django series.


At first we've to create virtual environment. command - pip install virtualenvwrapper-win. (for windows)

Later, install django at present directory.

Start app services.

Create a folder named template.

Keep all the UI files in template.

Place the url's in the correct location to join path.

Then, you are ready to run server by using command - python manage.py runserver.

Follow, the link that has generated in the terminal.

Later make migrations to migrate all the files.

Then, create a database for the required fields.

The dummy data given, was taken in the views.py file to get the dummy data to the database.

And, later we've to qequest the data as JSON file.

This was done by the command - 

Check herre,

https://stackoverflow.com/questions/59151057/retrieve-data-from-sql-server-database-in-json-format-using-python-command-line

example,

django-admin loaddata --formate=json -


Try this,

django-admin loaddata --formate=json -database=test app_lable.ModelName | django-admin loaddata --formate --database=prod -


Documentation & Support

Full documentation for the project is available at https://www.django-rest-framework.org/.

Thanks for Visiting.
