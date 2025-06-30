from main.extensions import db
from sqlalchemy.dialects.postgresql import JSON

class NavigationLink(db.Model):
    """
    Navigation items for the application menu.
    """
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(10), default="")
    endpoint = db.Column(db.String(100), nullable=False)
    order = db.Column(db.Integer, default=0)
    is_visible = db.Column(db.Boolean, default=True)
