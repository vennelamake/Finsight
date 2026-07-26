import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "finsight123")

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://username:password@localhost/finsight_project"
    )

    if DATABASE_URL.startswith("mysql://"):
        DATABASE_URL = DATABASE_URL.replace("mysql://", "mysql+pymysql://", 1)

    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False