class Config(object):
    '''# common configuration settings'''
    JWT_SECRET_KEY = b'\xb3\x14\xa3&f\xcc.\x89r\xe9hT\xaf\xd0z\x84:\x85\x14\x11Pf\xfa<?x\xef<\xec\x946\xeb\xaa\\\xa4\xc4"W\xfb\x07'
    
    
    # APIs that need to display documentation
    API_DOC_MEMBER = [
        "users", # blueprint name
        
    ]

class ProdConfig(Config):
    '''# configuration settings for production env'''
    pass

class DevConfig(Config):
    '''# configuration settings for development env'''
    DEBUG = True
    MONGODB_SETTINGS = {
    'db': 'flask_mongo',
    'host': 'localhost',
    'port': 27017
    }