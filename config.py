class Config:
    SECRET_KEY = "your_secret_key"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/finsight_project"

    SQLALCHEMY_TRACK_MODIFICATIONS = False