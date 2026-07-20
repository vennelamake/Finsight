from extensions import db
from datetime import datetime


class Income(db.Model):

    __tablename__ = "income"

    income_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    source = db.Column(db.String(100), nullable=False)

    amount = db.Column(db.Float, nullable=False)

    income_date = db.Column(db.Date, nullable=False)

    description = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )