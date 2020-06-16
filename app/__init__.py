from flask import Flask
# from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# app.config.from_object(Config)
POSTGRES = {
    'user': 'postgres',
    'pw': 'Anminhhung09041999',
    'db': 'craft',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
                                        %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

from app import routes, models