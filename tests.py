from unittest import TestCase

from app.validation import validations
from app.accounts import dao
from app import app

data = {
    "name": "Sekitoleko Baker",
    "email": "becks@gmail.com",
    "password": "mukunguB@01",
    "password2": "mukunguB@01"
}


class TestValidations(TestCase):
    def setUp(self):
        self.validator = validations.Validator()

    def test_validator_obj(self):
        self.assertIsInstance(self.validator, validations.Validator)

    def test_is_empty(self):
        self.assertFalse(self.validator.is_empty(data))

    def test_register_input_validation(self):
        self.assertEqual(
            len(self.validator.register_input_validation(data)["errors"]), 0)

    def test_validate_email(self):
        self.assertTrue(self.validator.validate_email(data["email"]))

    def test_validate_password(self):
        self.assertTrue(self.validator.validate_password(data["password"]))

    def test_login_input_validation(self):
        self.assertTrue(
            self.validator.login_input_validation(data)["is_true"])


class TestModels(TestCase):
    def setUp(self):
        pass


class TestDataAcess(TestCase):
    def setUp(self):
        self.dao_obj = dao.Account()

    def test_add_account(self):
        with app.app_context():
            self.assertEqual(self.dao_obj.add_account(data)[0], 200)


class TestAccountRoutes(TestCase):
    def setUp(self):
        pass


class TestTaskRoutes(TestCase):
    def setUp(self):
        pass
