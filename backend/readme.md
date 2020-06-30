# running the backend

## step 1: create a virtual environment
a virtual environment allows you to install packages for specific projects.
to create a virtual environment you can run `python3 -m venv env`

## step 2: start the virtual environment
after creating the environment you still need to start it.
on mac and linux you can run `source env/bin/activate`.
on windows run `.\env\Scripts\activate`.

## step 3: install the required packages
there is a requiremnts.txt file in the backend directory.
to install the packages simply run `pip install -r requirements.txt`

## step 4: set the environment variables
flask needs to know which file to run.
you can configure this using an environment variable.
on mac and linux run `export FLASK_APP=app.py`.
on windows you can run `set FLASK_APP=app.py` if you're using the command prompt.
if you're using powershell you can run `$env:FLASK_APP = "app.py"`.

## step 5: run the project
to run the project you can run `flask run`.
