import json


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
            errors.update({"password": "Password should not be blank"})

        return json.dumps(errors)
