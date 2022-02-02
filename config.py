import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "remember_to_add_scret-key"
    SQLALCHEMY_DATABASE_URL = (
        os.environ.get('DATABASE_URL') or
        'sqlite:///'+os.path.join(BASE_DIR, 'microblog.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False