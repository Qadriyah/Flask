import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from config import app_settings

app = Flask(__name__)
if os.environ.get("APP_ENV") == "testing":
    app.config.from_object(app_settings["testing"])
else:
    app.config.from_object(app_settings["development"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

#  import the models
from .models.model import *

#  Register blueprints
from .accounts import account as account_bp
app.register_blueprint(account_bp)

from .tasks import task as task_bp
app.register_blueprint(task_bp)
