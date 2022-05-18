The spimplest way to test it is to:
1. Clone the repository on your own computer.

2. Create a new virtual environment in the root folder (the one this file):

        python -m venv env

3. Activate the virtual environment
    + unix: source env/bin/activate
    + windows: env/Scripts/activate.bat

4. Install the dependencies via the requirement.txt file

        pip install -r requirements.txt

5. Run the server:

        python manage.py runserver

6. Click the link in your command line interface or copy the url in your web browser:
    Starting development server at http://127.0.0.1:8000/

Note: respect PEP8 thanks to flake8