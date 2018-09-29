from flask import request, render_template
import json

#  import account blueprint
from . import account
#  import account model
from app.models import account_model

account_db = account_model.Account()


@account.route("/account/new_account", methods=["POST"])
def add_account():
    if request.method == "POST":
        return "Good"


def login_user(self, name, password):
    pass
