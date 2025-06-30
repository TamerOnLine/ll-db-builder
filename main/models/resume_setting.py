from main.extensions import db
from sqlalchemy.dialects.postgresql import JSON

class Setting(db.Model):
    """
    Stores configuration settings as key-value pairs.
    """
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Text, nullable=False)