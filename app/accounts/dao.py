from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from flask import jsonify
from flask_jwt_extended import create_access_token
import datetime
import os

from app.models.model import User
from app import bcrypt
from app import jwt


class Account:

    def __init__(self):
        engine = create_engine(os.environ.get("DATABASE_URL"))
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
        password_hash = bcrypt.generate_password_hash(
            request_data["password"], 15)
        try:
            new_user = User(
                name=request_data["name"],
                email=request_data["email"],
                password=password_hash.decode("utf-8")
            )
            #  Check if user already exists
            if not self.is_user_exist(request_data["email"])[1]:
                self.session.add(new_user)
                self.session.commit()
                self.session.close()
                response.update({"msg": "User added successfully"})
                self.status_code = 200
            else:
                response.update({"msg": "User already exists"})
                self.status_code = 401

        except SQLAlchemyError as err:
            response.update({"db_error": "Unable to add user to the database"})
            self.status_code = 500
        return jsonify(response), self.status_code

    def login_user(self, request_data):
        response = {}
        #  Check if user exists
        result = self.is_user_exist(request_data["email"])
        if not result[1]:
            response.update({"errors": "Wrong email or password"})
            self.status_code = 401
        else:
            #  Check if password provided matches one in the database
            if bcrypt.check_password_hash(
                    result[0].password, request_data["password"]):
                #  Create jwt payload
                jwt_payload = {
                    "id": result[0].id,
                    "name": result[0].name,
                    "email": result[0].email
                }
                #  Create token
                token = create_access_token(
                    jwt_payload, expires_delta=datetime.timedelta(days=7))
                response.update({
                    "success": True,
                    "token": "Bearer {}".format(token)
                })
                self.status_code = 200
            else:
                response.update({"error": "Wrong email or password"})
                self.status_code = 401

        return jsonify(response), self.status_code

    def is_user_exist(self, email):
        result = self.session.query(User).filter(
            User.email == "{}".format(email)).first()

        if result:
            return result, True
        return "", False
