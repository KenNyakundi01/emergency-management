import os

class Config:
	'''
	parent configuration
	'''
	SQLALCHEMY_TRACK_MODIFICATIONS=False

	    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "beresnasam123@gmail.com"
    MAIL_PASSWORD = "sams1234"
    SUBJECT_PREFIX = 'emergency-management'
    SENDER_EMAIL = 'beresnasam123@gmail.com'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}