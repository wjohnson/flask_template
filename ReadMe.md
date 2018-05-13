# A Quick Template for Flask Apps

This is my personal template for creating flask applications that require user authentication.  It draws heavily from Miguel Greenberg's incredible [Flask Mega Tutorial](https://learn.miguelgrinberg.com/) and uses [Bootstrap.js](https://getbootstrap.com/docs/3.3/getting-started/#template) for a nice responsive design.

This template is available for you to use, but comes with no guarantee or warranty.  Use at your own risk.

# Getting up and Running

    virtualenv env
    source ./env/bin/activate
    pip install -r requirements.txt
    export FLASK_APP=apprunner.py
    flask db init
    flask db migrate -m "Users table"
    flask db upgrade
    flask run
