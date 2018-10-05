import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Common configurations"""
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY: "mukunguB"


class DevelopmentConfig(Config):
    """Development configurations"""
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]


class TestingConfig(Config):
    """Testing configurations"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")


class ProductionConfig(Config):
    """Production configurations"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRES_DATABASE_URL")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")


app_settings = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "production": "config.ProductionConfig"
}
