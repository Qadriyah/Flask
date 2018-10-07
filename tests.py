from unittest import TestCase
import json

from app.validation import validations
from app.accounts import dao
from app import app

data = {
    "name": "Sekitoleko Baker",
    "email": "henry@gmail.com",
    "password": "mukunguB@3",
    "password2": "mukunguB@3"
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

    def test_is_user_exists(self):
        with app.app_context():
            self.assertTrue(self.dao_obj.is_user_exist(data["email"])[1])

    def test_add_account(self):
        with app.app_context():
            if not self.dao_obj.is_user_exist(data["email"])[1]:
                self.assertEqual(json.loads(self.dao_obj.add_account(
                    data)[0].get_data().decode("utf-8"))["msg"], "User added successfully")

    def test_login_user(self):
        with app.app_context():
            self.assertEqual(self.dao_obj.login_user(data)[1], 200)


class TestAccountRoutes(TestCase):
    def setUp(self):
        pass


class TestTaskRoutes(TestCase):
    def setUp(self):
        pass
