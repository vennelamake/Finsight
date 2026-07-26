import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "finsight123")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://username:password@localhost/finsight_project"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False