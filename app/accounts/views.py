from flask import request, jsonify
import json

#  import account blueprint
from . import account
#  import account data access object
from . import dao
#  import validations
from app.validation import validations

data_access_obj = dao.Account()
validator = validations.Validator()


@account.route("/account/new_account", methods=["POST"])
def add_account():
    """
    This creates an account on the system that authorizes the 
    user to access system resources
    """
    if request.method == "POST":
        result = validator.register_input_validation(request.form)
        if not result["is_true"]:
            return jsonify(result["errors"]), 400
        return data_access_obj.add_account(request.form)


@account.route("/account/login", methods=["POST"])
def login_user():
    """
    This authenticates the user and returns a JWT token for making
    subsequent requests
    """
    if request.method == "POST":
        #  Validate user input
        if not validator.login_input_validation(request.form)["is_true"]:
            return jsonify(result["errors"]), 400
        return data_access_obj.login_user(request.form)
