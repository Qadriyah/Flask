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
    todo = relationship("Todo", back_populates="user",
                        cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<User(id={}, name={}, email={})>".format(self.id, self.name, self.email)


class Todo(db.Model):
    """Todo model"""

    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User", back_populates="todo")
    todoitem = relationship("TodoItem", back_populates="todo")

    def __repr__(self):
        return "<Todo(id={}, name={}, status={}, user_id={})>".format(self.id, self.name, self.status, self.user_id)


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
    todo = relationship("Todo", back_populates="todoitem")

    def __repr__(self):
        return "<TodoItem(id={}, name={}, description={}, status={}, due_at={}, todo_id={})>".format(self.id, self.name, self.description, self.status, self.due_at, self.todo_id)
