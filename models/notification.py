from extensions import db
from datetime import datetime

class Notification(db.Model):
    __tablename__ = "notifications"

    notification_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    title = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)

    type = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(30), nullable=False)

    is_read = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)