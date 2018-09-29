from flask import Flask, request

app = Flask(__name__)

#  Register blueprints
from .accounts import account as account_bp
app.register_blueprint(account_bp)

from .tasks import task as task_bp
app.register_blueprint(task_bp)
