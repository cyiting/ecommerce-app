from flask import Flask, request, make_response, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

import datetime

MYSQL_USER = "users_db"
MYSQL_PASSWORD = "users_db"
MYSQL_DB = "users_db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@localhost:3306/{MYSQL_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())
    address = db.relationship('Address', backref='user', lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_line1 = db.Column(db.String(255), nullable=False)
    address_line2 = db.Column(db.String(255))
    country = db.Column(db.String(32), nullable=False)
    postal_code = db.Column(db.String(16), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, address_line1, address_line2, country, postal_code):
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.country = country
        self.postal_code = postal_code

@app.route("/create_user", methods=['POST'])
def create_user():
    data = json.loads(request.data)
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    password = data['password']

    try:
        new_user = User(first_name, last_name, email, password)
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        response = make_response("Email already in use")
        response.status_code = 409
        return response

    response = make_response("Success")
    response.status_code = 200
    return response
