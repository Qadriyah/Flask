from flask import request, render_template, jsonify, Response
import json

#  import account blueprint
from . import account
#  import account model
from app.models import account_model
#  import validations
from app.validation import validations

account_db = account_model.Account()
validator = validations.Validator()


@account.route("/account/new_account", methods=["POST"])
def add_account():
    if request.method == "POST":
        result = validator.register_validation(request.form)
        if not result["is_true"]:
            return jsonify(result["errors"]), 400
        return 200


def login_user(self, name, password):
    pass
