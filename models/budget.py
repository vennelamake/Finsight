from extensions import db
from datetime import datetime


class Budget(db.Model):

    __tablename__ = "budgets"

    budget_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    budget_amount = db.Column(db.Float, nullable=False)

    budget_month = db.Column(db.String(20), nullable=False)

    budget_year = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )