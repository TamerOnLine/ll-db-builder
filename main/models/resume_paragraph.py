from main.extensions import db
from sqlalchemy.dialects.postgresql import JSON

class ResumeParagraph(db.Model):
    """
    Paragraph unit under a resume section.
    """
    id = db.Column(db.Integer, primary_key=True)
    resume_section_id = db.Column(db.Integer, db.ForeignKey('resume_section.id'), nullable=False)
    field_type = db.Column("type", db.String(50), nullable=False)  # e.g., basic, with_description, with_date
    order = db.Column(db.Integer, nullable=False)
    is_visible = db.Column(db.Boolean, default=True)
    location = db.Column(db.String(50), default="main")
    title_translations = db.Column(JSON, nullable=True)

    fields = db.relationship(
        "ResumeField",
        back_populates="paragraph",
        cascade="all, delete-orphan",
        lazy=True
    )
