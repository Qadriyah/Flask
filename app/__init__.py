from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#  Register blueprints
from .accounts import account as account_bp
app.register_blueprint(account_bp)

from .tasks import task as task_bp
app.register_blueprint(task_bp)
