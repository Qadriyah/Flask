from unittest import TestCase
from app.validation import validations


class TestValidations(TestCase):
    def setUp(self):
        self.validator = validations.Validator()
        self.data = {
            "name": "Sekitoleko Baker",
            "email": "becks@gmail.com",
            "password": "mukunguB@01",
            "password2": "mukunguB@01"
        }

    def test_validator_obj(self):
        self.assertIsInstance(self.validator, validations.Validator)

    def test_is_empty(self):
        self.assertFalse(self.validator.is_empty(self.data))

    def test_register_input_validation(self):
        self.assertTrue(
            self.validator.register_input_validation(self.data)["is_true"])
        self.assertEqual(
            len(self.validator.register_input_validation(self.data)["errors"]), 0)

    def test_validate_email(self):
        self.assertTrue(self.validator.validate_email(self.data["email"]))

    def test_validate_password(self):
        self.assertTrue(self.validator.validate_password(
            self.data["password"]))

    def test_login_input_validation(self):
        self.assertTrue(
            self.validator.login_input_validation(self.data)["is_true"])


class TestModels(TestCase):
    def setUp(self):
        pass


class TestDataAcess(TestCase):
    def setUp(self):
        pass


class TestAccountRoutes(TestCase):
    def setUp(self):
        pass


class TestTaskRoutes(TestCase):
    def setUp(self):
        pass
