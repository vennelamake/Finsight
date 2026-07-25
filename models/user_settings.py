from extensions import db
from datetime import datetime


class UserSettings(db.Model):
    __tablename__ = "user_settings"

    setting_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        unique=True,
        nullable=False
    )

    # Currency Settings
    currency = db.Column(db.String(10), default="INR")
    exchange_rate = db.Column(db.Float, default=1.0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    # Theme
    theme = db.Column(db.String(10), default="light")

    # Notifications
    budget_alert = db.Column(db.Boolean, default=True)
    income_notification = db.Column(db.Boolean, default=True)
    expense_notification = db.Column(db.Boolean, default=True)
    savings_notification = db.Column(db.Boolean, default=True)
    goal_reminder = db.Column(db.Boolean, default=True)
    investment_update = db.Column(db.Boolean, default=True)
    financial_health_alert = db.Column(db.Boolean, default=True)
    spending_insight = db.Column(db.Boolean, default=True)