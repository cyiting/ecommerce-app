from flask import Flask
from dotenv import load_dotenv

from config import Config
from app.database import db
from app.blueprints.authentication import authentication
from app.blueprints.user_management import user_management

def create_app(config_class=Config):
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(authentication)
    app.register_blueprint(user_management)

    return app