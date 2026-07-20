from extensions import db
from datetime import date

class Investment(db.Model):

    __tablename__ = "investments"

    investment_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    investment_name = db.Column(db.String(100), nullable=False)

    investment_type = db.Column(db.String(50), nullable=False)

    symbol = db.Column(db.String(50), nullable=True)

    quantity = db.Column(db.Float, nullable=False)

    buy_price = db.Column(db.Float, nullable=False)

    current_price = db.Column(db.Float, nullable=False)

    purchase_date = db.Column(db.Date, default=date.today)

    created_at = db.Column(db.DateTime, server_default=db.func.now())