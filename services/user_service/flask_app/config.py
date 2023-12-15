import os

basedir = os.path.abspath(os.path.dirname(__file__))

mysql_user = os.environ.get('MYSQL_USER')
mysql_password = os.environ.get('MYSQL_PASSWORD')
mysql_db = os.environ.get('MYSQL_DB')
db_uri = f"mysql://{mysql_user}:{mysql_password}@localhost/{mysql_db}"

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False