set virtual environment on Windows:  
https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html

if `.\venv\Scripts\activate` doesn't work

- and get back this error `.\venv\Scripts\activate : File [path to your file] cannot be loaded because running scripts is disabled on this system.`
- run this `Set-ExecutionPolicy Unrestricted -Force` (for Windows Users)

for devlopers (my case: on Windows):  
when the jinja files are changed, the server is not restarted.

- to make it restart, save the app.py file( `ctrl` + `s`)
- reload the browser, the new changes will appeare


changes from laptop