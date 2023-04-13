class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'mydata232@gmail.com'
    MAIL_PASSWORD = 'Dummy@12'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

