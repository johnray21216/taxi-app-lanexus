import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/taxi"
    RIDE_COMPLETION_DURATION_IN_SEC = 300
    DRIVER_THRESHOLD = 5
    REDIS = {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
        "PASSWORD": None
    }

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgres://nrnwcdimbpjbqg:7831089f7d0f099618f7e575ce57d4d06ace"


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
