from flask import Blueprint

user_management = Blueprint('user_management', __name__)

@user_management.route('/testuser')
def test():
    return "user"