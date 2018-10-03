from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from flask import jsonify
import bcrypt
import os

from app.models.model import User


class Account:

    def __init__(self):
        engine = create_engine(os.environ["DATABASE_URL"])
        #  Initialize a session class
        Session = sessionmaker()
        #  Connect to the session
        Session.configure(bind=engine)
        #  Create a session object
        self.session = Session()
        self.status_code = 200

    def add_account(self, request_data):
        response = {}
        #  Hash password
        password_hash = bcrypt.hashpw(
            request_data["password"].encode("utf-8"), bcrypt.gensalt(15))
        try:
            new_user = User(
                name=request_data["name"],
                email=request_data["email"],
                password=password_hash
            )
            result = self.session.query(User).filter(
                User.email == "{}".format(request_data["email"])).first()
            #  Check if user already exists
            if not result:
                self.session.add(new_user)
                self.session.commit()
                self.session.close()
                response.update({"msg": "User added successfully"})
            else:
                response.update({"msg": "User already exists"})
                self.status_code = 401

        except:
            response.update({"db_error": "Unable to add user to the database"})
            self.status_code = 500
        return jsonify(response), self.status_code

    def login_user(self, name, password):
        pass
