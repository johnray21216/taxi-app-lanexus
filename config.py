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
        "HOST": "redis-15374.c8.us-east-1-3.ec2.cloud.redislabs.com",
        "PORT": 15374,
        "DB": 0,
        "PASSWORD": "jNLs0cU9hHMpsqvhXMEAyUkkOGHTsvSf"
    }

class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgres://txhkoxgkqkogma:86e4c5354dff460b90b14ea14e42dfc5314e2d80e55181a3fedcd0cc1a021d08@ec2-44-196-223-128.compute-1.amazonaws.com:5432/d8fb20pvpuls1p"


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
