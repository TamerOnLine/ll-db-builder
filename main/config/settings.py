# settings.py

import os
from main.config.config_loader import load_env_config

class Config:
    """
    Central configuration class for the Flask application.

    Attributes:
        SECRET_KEY (str): Secret key for Flask sessions and security.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Disable Flask-SQLAlchemy event notifications.
        DEBUG (bool): Flask debug mode flag.
        DB_NAME (str): Database name.
        DB_USER (str): Database username.
        DB_PASSWORD (str): Database password.
        DB_HOST (str): Database host.
        DB_PORT (int): Database port.
        SQLALCHEMY_DATABASE_URI (str): URI used by SQLAlchemy to connect to the database.
    """

    config = load_env_config()

    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = config.get("FLASK_DEBUG", "True") == "True"

    # PostgreSQL connection settings from .env
    DB_NAME = config["DB_NAME"]
    DB_USER = config["DB_USER"]
    DB_PASSWORD = config["DB_PASSWORD"]
    DB_HOST = config["DB_HOST"]
    DB_PORT = config["DB_PORT"]

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
