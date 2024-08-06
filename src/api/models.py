from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    avatar=db.Column(db.String(200),nullable=False)
    name=db.Column(db.String(20),nullable=False)
    last_name=db.Column(db.String(20),nullable=False)
    username=db.Column(db.String(30), unique=True,nullable=False)
    password = db.Column(db.String(10), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.avatar}{self.name}{self.last_name}{self.username}>'

    def serialize(self):
        return {
            "id": self.id,
            "avatar": self.avatar,
            "name": self.name,
            "last_name": self.last_name,
            "username": self.username,
        }