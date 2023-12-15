from app.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)

    def __init__(self, first_name, last_name, username, email, password, created_at):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at