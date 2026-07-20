from extensions import db


class InvestmentTransaction(db.Model):

    __tablename__ = "investment_transactions"

    transaction_id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        nullable=False
    )

    investment_id = db.Column(
        db.Integer,
        nullable=False
    )

    transaction_type = db.Column(
        db.String(10),
        nullable=False
    )

    quantity = db.Column(
        db.Float,
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    transaction_date = db.Column(
        db.Date,
        nullable=False
    )