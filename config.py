import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Common configurations"""
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY: "mukunguB"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]


class DevelopmentConfig(Config):
    """Development configurations"""
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """Testing configurations"""
    TESTING = True


class ProductionConfig(Config):
    """Production configurations"""
    DEBUG = False
