from flask import Flask
from  flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dd8abf76ec7abe0f3f6b73565c8f579f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from flaskapp import routes