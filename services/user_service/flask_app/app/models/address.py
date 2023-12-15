from app.database import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_line1 = db.Column(db.String(255), nullable=False)
    address_line2 = db.Column(db.String(255))
    postal_code = db.Column(db.String(16), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, address_line1, address_line2, postal_code, user_id):
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.postal_code = postal_code
        self.user_id = user_id
