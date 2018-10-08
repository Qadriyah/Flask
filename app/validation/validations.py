import re


class Validator:

    def __init__(self):
        self.regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

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

    def register_input_validation(self, request_data):
        """
        Validates input data from the registration form

        Args:
            request_data(object): request Object that holds form data

        Retruns:
            dict: {"errors", True} if there were any errors {"", False} if there were no errors
        """
        errors = {}
        #  validate name
        if not request_data["name"]:
            errors.update({"name": "Name is required"})

        #  validate email
        if not self.validate_email(request_data["email"]):
            errors.update({"email": "Your email address is invalid"})

        #  validate password
        if not self.validate_password(request_data["password"]):
            errors.update(
                {"password": "Your password should be at least 8 characters, contain a lowercase letter, uppercase letter, a digit and a character"})

        #  check if passwords match
        if request_data["password"] != request_data["password2"]:
            errors.update({"mismatch": "Your passwords do not match"})

        return {
            "errors": errors,
            "is_true": self.is_empty(errors)
        }

    def validate_email(self, email):
        """
        Checks if email is a valid email address

        Args:
            email(str): User's email address

        Returns:
            bool: True if email is valid, False otherwise
        """
        if not email or\
                not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return False
        return True

    def validate_password(self, password):
        """
        Checks if password contains lowercase, uppercase, character, number and 
        is at least 8 characters long

        Args:
            password(str): User's password

        Returns:
            bool: True if password matches all options, False otherwise
        """
        if not password or not re.match(self.regex, password):
            return False
        return True

    def login_input_validation(self, request_data):
        """
        Validates input data from the login form

        Args:
            request_data(object): request object that holds form data

        Returns:
            dict: {"errors", True} if any errors found, {"", False} if no
            errors found
        """
        errors = {}
        if not self.validate_email(request_data["email"]) or\
                not self.validate_password(request_data["password"]):
            errors.update({"login": "Wrong email or password"})

        return {
            "errors": errors,
            "is_true": self.is_empty(errors)
        }
