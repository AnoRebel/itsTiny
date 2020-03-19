import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base config vars."""

    DEBUG = False
    TESTING = False
    ENV = "production"
    FLASK_ENV = "production"
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(64)  # os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = "slate"


class ProdConfig(Config):
    """ Production Configs inheriting from Base Config """

    # Database Configs
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_ECHO = False


class DevConfig(Config):
    """ Development Configs Inheriting from Base Config """

    DEBUG = True
    TESTING = True
    ENV = "development"
    FLASK_ENV = "development"
    # Database Configs
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URI")
    SQLALCHEMY_ECHO = True
