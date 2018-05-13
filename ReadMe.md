# Getting up and Running

    export FLASK_APP=apprunner.py
    flask db init
    flask db migrate -m "Users table"
    flask db upgrade
    flask run
