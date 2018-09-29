import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Common configurations"""
    DEBUG = True,
    TESTING = False,
    CSRF_ENABLED = True
    SECRET_KEY: "mukunguB"
    SQLALCHEMY_DATABSE_URI = os.environ["DATABASE_URI"]


class DevelopmentConfig:
    """Development configurations"""
    DEVELOPMENT = True,
    DEBUG = True


class TestingConfig:
    """Testing configurations"""
    TESTING = True


class ProductionConfig:
    """Production configurations"""
    DEBUG = False
