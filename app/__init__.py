from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

appvar = Flask(__name__)
appvar.config.from_object(Config)
#appvar.config['TESTING'] = False

db = SQLAlchemy(appvar)
migrate = Migrate(appvar, db)

login = LoginManager(appvar)
login.login_view = 'login'

from app import routes, models
