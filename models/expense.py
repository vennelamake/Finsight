from extensions import db
from datetime import datetime


class Expense(db.Model):

    __tablename__ = "expenses"

    expense_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.user_id"),
                        nullable=False)

    category = db.Column(db.String(50), nullable=False)

    amount = db.Column(db.Float, nullable=False)

    description = db.Column(db.String(255))

    payment_method = db.Column(db.String(50))

    expense_date = db.Column(db.Date,
                             default=datetime.utcnow)

    created_at = db.Column(db.DateTime,
                           default=datetime.utcnow)