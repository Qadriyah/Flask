from app import db
from datetime import datetime
from sqlalchemy.orm import relationship


class User(db.Model):
    """User model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    todos = relationship("Todo", back_populates="users",
                         cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<id {}>".format(self.id)


class Todo(db.Model):
    """Todo model"""

    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User", back_populates="todos")

    def __repr__(self):
        return "<id {}>".format(self.id)


class TodoItem(db.Model):
    """Toto Item model"""

    __tablename__ = "todoitems"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    due_at = db.Column(db.Date)
    todo_id = db.Column(db.Integer, db.ForeignKey("todos.id"))
    todo = relationship("Todo", back_populates="todoitems")

    def __repr__(self):
        return "<id {}>".format(self.id)
