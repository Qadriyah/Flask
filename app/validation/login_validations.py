from . import register_validations


class LoginValidator:

    def __init__(self):
        self.reg_validator = register_validations.Validator()

    def login_input_validation(self, data):
        errors = {}
        if not self.reg_validator.validate_email(data["email"]):
            errors.update({"email": "Your email address is not valid"})

        if not self.reg_validator.validate_password(data["password"]):
            errors.update({"password": "Wrong password"})

        return {
            "errors": errors,
            "is_true": self.reg_validator.is_empty(errors)
        }
