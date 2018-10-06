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

        except SQLAlchemyError as err:
            response.update({"db_error": err})
            self.status_code = 500
        return jsonify(response), self.status_code

    def login_user(self, request_data):
        response = {}
        result = self.session.query(User).filter(
            User.email == "{}".format(request_data["email"])).first()
        #  Check if user exists
        if not result:
            response.update({"error": "Wrong email or password"})
            self.status_code = 401
        else:
            #  Check if password provided matches on in the database
            if bcrypt.check_password_hash(
                    result.password, request_data["password"]):
                #  Create jwt payload
                jwt_payload = {
                    "id": result.id,
                    "name": result.name,
                    "email": result.email
                }
                #  Create token
                token = create_access_token(
                    jwt_payload, expires_delta=datetime.timedelta(days=7))
                response.update({
                    "success": True,
                    "token": "Bearer {}".format(token)
                })
            else:
                response.update({"error": "Wrong email or password"})
                self.status_code = 401

        return jsonify(response), self.status_code
