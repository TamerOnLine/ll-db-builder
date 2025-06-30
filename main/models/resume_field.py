from main.extensions import db

class ResumeField(db.Model):
    """
    Field unit inside a paragraph.
    """
    id = db.Column(db.Integer, primary_key=True)
    resume_paragraph_id = db.Column(db.Integer, db.ForeignKey('resume_paragraph.id'), nullable=False)
    field_type = db.Column("type", db.String(500), nullable=False)  # e.g., text, link, email
    order = db.Column(db.Integer, nullable=False)
    is_visible = db.Column(db.Boolean, default=True)
    label = db.Column(db.String(200), nullable=True)
    value = db.Column(db.String(500), nullable=True)
    description = db.Column(db.String(500), nullable=True)  # ✅ هذا هو السطر الصحيح

    paragraph = db.relationship("ResumeParagraph", back_populates="fields")
