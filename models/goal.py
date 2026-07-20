from extensions import db
from datetime import datetime


class Goal(db.Model):

    __tablename__ = "goals"

    goal_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    goal_name = db.Column(db.String(100), nullable=False)

    target_amount = db.Column(db.Float, nullable=False)

    saved_amount = db.Column(db.Float, default=0)

    target_date = db.Column(db.Date, nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )