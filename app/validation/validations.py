import re


class Validator:

    def is_empty(self, value):
        """Checks if an object is empty

        Args:
            value(object): can be a dict or a str

        Returns:
            bool: True for empty, False otherwise
        """
        if value == None or value is None or (type(value) == dict and len(value) == 0) or (type(value) == str and len(value.strip()) == 0):
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
        #  validate name
        if not request_data["name"]:
            errors.update({"name": "Name is required"})

        #  validate email
        if not request_data["email"]:
            errors.update({"email": "Email is required"})

        #  validate password
        if not request_data["password"]:
            errors.update({"password": "Password is required"})

        #  validate password2
        if not request_data["password2"]:
            errors.update({"password": "Password2 is required"})

        #  check if passwords match
        if request_data["password"] != request_data["password2"]:
            errors.update({"mismatch": "Your passwords do not match"})

        #  Check if the password meets the standards
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", request_data["password"]):
            errors.update(
                {"weak_pass": "Your password should be at least 8 characters, contain a lowercase letter, uppercase letter, a digit and a character"})

        # validate email format
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                        request_data["email"]):
            errors.update({"invalid_email": "Your email is invalid"})

        return {
            "errors": errors,
            "is_true": self.is_empty(errors)
        }
