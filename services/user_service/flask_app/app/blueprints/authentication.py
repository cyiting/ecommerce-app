from flask import Blueprint

authentication = Blueprint('authentication', __name__)

@authentication.route('/testauth')
def test():
    return "auth"