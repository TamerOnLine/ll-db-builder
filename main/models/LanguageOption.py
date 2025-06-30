from main.extensions import db
from sqlalchemy.dialects.postgresql import JSON


class LanguageOption(db.Model):
    """
    Supported languages for localization.
    """
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    order = db.Column(db.Integer, default=0)
    is_visible = db.Column(db.Boolean, default=True)