from datetime import datetime
from flask_login import current_user
from flask import session
from models.user_settings import UserSettings


def time_ago(dt):
    if dt is None:
        return ""

    now = datetime.utcnow()
    diff = now - dt

    if diff.days == 0:
        if diff.seconds < 60:
            return "Just now"
        elif diff.seconds < 3600:
            mins = diff.seconds // 60
            return f"{mins} min ago"
        else:
            hrs = diff.seconds // 3600
            return f"{hrs} hr ago"

    elif diff.days == 1:
        return "1 day ago"

    elif diff.days < 7:
        return f"{diff.days} days ago"

    elif diff.days < 30:
        weeks = diff.days // 7
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"

    else:
        months = diff.days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"


# ---------------------------------------
# Currency Conversion Helper
# ---------------------------------------

def convert_currency(amount):

    if amount is None:
        amount = 0

    settings = UserSettings.query.filter_by(
        user_id=current_user.user_id
    ).first()

    symbols = {
        "INR": "₹",
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
        "AUD": "A$",
        "CAD": "C$",
        "AED": "د.إ",
        "SGD": "S$"
    }

    if settings is None:
        return {
            "amount": round(amount, 2),
            "symbol": "₹"
        }

    converted = amount * (settings.exchange_rate or 1.0)

    return {
        "amount": round(converted, 2),
        "symbol": symbols.get(settings.currency, "₹")
    }

def convert_amount(amount):
    return convert_currency(amount)["amount"]

def convert_to_base_currency(amount):
    """Convert selected currency back to INR before saving."""
    rate = session.get("exchange_rate", 1)

    if rate == 0:
        return amount

    return amount / rate

def get_currency_symbol():
    settings = UserSettings.query.filter_by(
        user_id=current_user.user_id
    ).first()

    symbols = {
        "INR": "₹",
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
        "AUD": "A$",
        "CAD": "C$",
        "AED": "د.إ",
        "SGD": "S$"
    }

    if settings:
        return symbols.get(settings.currency, "₹")

    return "₹"


def convert_list(values):
    return [convert_amount(value) for value in values]