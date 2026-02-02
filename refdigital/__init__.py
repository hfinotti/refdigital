from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

#if os.getenv("DATABASE_URL"):
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
#else:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///refdigital.db'

app.config['SECRET_KEY'] = "tlzOLzw7lax4nOLorzNJiJG8uhpumgKx"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "admin"

from refdigital import routes