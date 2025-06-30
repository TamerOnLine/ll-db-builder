from main.extensions import db
from sqlalchemy.dialects.postgresql import JSON

class ResumeSection(db.Model):
    """
    Resume section with language support and visibility toggle.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    lang = db.Column(db.String(10), nullable=False, default='en')
    is_visible = db.Column(db.Boolean, default=True)
    title_translations = db.Column(JSON, nullable=True)

    paragraphs = db.relationship(
        "ResumeParagraph",
        backref="resume_section",
        cascade="all, delete-orphan",
        lazy=True
    )
