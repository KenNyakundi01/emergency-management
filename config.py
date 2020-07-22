import os

class Config:
	'''
	parent configuration
	'''
	SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}