from main.extensions import db
from sqlalchemy.dialects.postgresql import JSON

class SidebarLink(db.Model):
    __tablename__ = "sidebar_link"

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100), nullable=False)  # اسم الزر أو الرابط
    endpoint = db.Column(db.String(200), nullable=False)  # اسم المسار (url_for)
    icon = db.Column(db.String(50), nullable=True)  # رمز أيقونة (اختياري)
    order = db.Column(db.Integer, default=0)  # ترتيب العرض
    is_visible = db.Column(db.Boolean, default=True)  # لإخفاء/عرض الرابط
