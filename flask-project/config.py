# Common
class Config(object):
    '''
    ### common config settings here
    any message goes here
    '''
    pass

# Production
class ProdConf(Config):
    '''### config for production'''
    pass

# Development
class DevConf(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
    'db': 'flask_mongo',
    'host': '127.0.0.1',
    'port': 27017
    }