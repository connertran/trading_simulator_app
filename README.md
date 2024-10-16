set virtual environment on Windows:  
https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html

if `.\venv\Scripts\activate` doesn't work

- and get back this error `.\venv\Scripts\activate : File [path to your file] cannot be loaded because running scripts is disabled on this system.`
- run this `Set-ExecutionPolicy Unrestricted -Force` (for Windows Users)

for devlopers (my case: on Windows):  
when the jinja files are changed, the server is not restarted.

- to make it restart, save the app.py file( `ctrl` + `s`)
- reload the browser, the new changes will appeare

Create two PostgreSQL databases for the project: one for the app (trading_db) and one for app testing (trading_test).

working with flask_migrate (similar when commiting the changes with git): flask_migrate helps you update the database, when the 'sqlalchemy' file is changed.

1. `flask db init`

- This will create a 'migrations directory' where Alembic will store migration scripts.

2. `flask db migrate -m "Describe your migration here"`

- This will generate a migration script that reflects the changes made to your models.

3. `flask db upgrade`

- This command will apply the new migration script to update your database schema without dropping or recreating the database.
