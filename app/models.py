from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class TimestampMixin(object):
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)


class User(TimestampMixin, UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin_rights = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self):
        return self.admin_rights == 1

class Profession(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(31))
    # This enables reversing the foreign key
    # i.e. look up all parents based on the profession.
    parents = db.relationship("Parent",backref="objective",lazy="dynamic")


# Example Many to Many table relationship
many_to_many_table = db.Table('M_to_M_table_name',
    db.Column('parent_id', db.Integer, db.ForeignKey('parent.id'), primary_key=True),
    db.Column('child_id', db.Integer, db.ForeignKey('child.id'), primary_key=True)
    )


class Parent(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    # Example Foreign Key Reference
    profession_id = db.Column(db.Integer, db.ForeignKey('profession.id'))
    # How to reference a many-to-many table 
    # variable = (Model, secondary = variable storing M:M, backref = name when reversed (attribute for children))
    children = db.relationship("Child", secondary=many_to_many_table, backref=db.backref("parents",lazy=True),lazy="subquery")

    def __repr__(self):
        return '<Parent {}>'.format(self.name)


class Child(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    
    def __repr__(self):
        return '<Child {}>'.format(self.name)
