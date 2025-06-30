from main.extensions import db
from sqlalchemy.dialects.postgresql import JSON

class Section(db.Model):
    """
    Core section table.
    """
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)