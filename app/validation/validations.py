import re


class Validator:

    def is_empty(self, value):
        """Checks if an object is empty

        Args:
            value(object): can be a dict or a str

        Returns:
            bool: True for empty, False otherwise
        """
        none = value == None or value is None
        dict_len = type(value) == dict and len(value) == 0
        str_len = type(value) == str and len(value.strip()) == 0
        if none or dict_len or str_len:
            return True
        return False

    def register_validation(self, request_data):
        """
        Validates input data for the registration form

        Args:
            request_data(object): Object that holds form data

        Retruns:
            dict: with two elements, a bool and a dict holding all errors that occured
            True if there were any errors, False otherwise
        """
        errors = {}
        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        #  validate name
        if not request_data["name"]:
            errors.update({"name": "Name is required"})

        #  validate email
        if not request_data["email"] or not re.match(email_regex, request_data["email"]):
            errors.update({"email": "Your email is invalid"})

        #  validate password
        if not request_data["password"] or not re.match(regex, request_data["password"]):
            errors.update(
                {"password": "Your password should be at least 8 characters, contain a lowercase letter, uppercase letter, a digit and a character"})

        #  check if passwords match
        if request_data["password"] != request_data["password2"]:
            errors.update({"mismatch": "Your passwords do not match"})

        return {
            "errors": errors,
            "is_true": self.is_empty(errors)
        }
