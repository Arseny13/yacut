from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import Config


app = Flask(__name__,
            static_folder='html',
            template_folder='html')
app.config.from_object(Config)
db = SQLAlchemy(app)

from . import  views, api_views, error_handlers