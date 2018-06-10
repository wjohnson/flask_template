import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    db_name = os.environ.get('DB_NAME')
    server_name = os.environ.get('SERVER_NAME')
    usr = os.environ.get('DB_USER')
    pw = os.environ.get('DB_PWD')
    PYODBC_CON = r'Driver={{ODBC Driver 13 for SQL Server}};Server=tcp:{server_name}.database.windows.net,1433;Database={db_name};Uid={usr}@{server_name};Pwd={pw};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'.format(
        server_name = server_name,
        db_name = db_name,
        usr = usr,
        pw = pw
    )
    if db_name is None:
        sqlAlchCON = None
    else:
        sqlAlchCON = "mssql+pyodbc://{usr}@{server_name}:{pw}@{server_name}.database.windows.net:1433/{db_name}?driver=ODBC+Driver+13+for+SQL+Server".format(
            server_name = server_name,
            db_name = db_name,
            usr = usr,
            pw = pw
        )

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET-KEY'
    SQLALCHEMY_DATABASE_URI = sqlAlchCON or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False