class Config:
    SECRET_KEY = "finsight123"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/finsight_project"

    SQLALCHEMY_TRACK_MODIFICATIONS = False