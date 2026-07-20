from extensions import db
from flask_login import UserMixin


class User(UserMixin, db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)

    fullname = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    mobile = db.Column(db.String(15), nullable=False)

    password = db.Column(db.String(255), nullable=False)

    profile_image = db.Column(db.String(255), default="default.png")

    occupation = db.Column(db.String(100))

    monthly_income = db.Column(db.Float)

    income_source = db.Column(db.String(100))

    risk_level = db.Column(db.String(30))

    financial_goal = db.Column(db.String(100))

    role = db.Column(db.String(20), default="User")

    is_verified = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    @property
    def id(self):
        return self.user_id

    def __repr__(self):
        return f"<User {self.fullname}>"