"""
For initializing redis connection pool. Any utility functions related to redis operations will reside here.
"""

import redis, logging
from taxi import app

__redis_conn_pool__ = redis.ConnectionPool(host=app.config['REDIS'].get('HOST', 'localhost'),
                                       port=app.config['REDIS'].get('PORT', 6379),
                                       db=app.config['REDIS'].get('DB', 0),
                                       password=app.config['REDIS'].get('PASSWORD', None))
redis_connection = redis.Redis(connection_pool=__redis_conn_pool__)
logging.basicConfig()
logger = logging.getLogger('redis')
logger.setLevel(logging.DEBUG)
logger.propagate = True