
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel

db = SQLAlchemy()
babel = Babel()

Base = db.Model  # Fix: Ensure models based on db.Model are picked up
