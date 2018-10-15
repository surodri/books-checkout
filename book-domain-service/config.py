import os

class Config(object):

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DB = 'schema.db'


class Config_Test(object):
    
    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASEDIR, 'test/test_database.db')
     
    #SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    TESTING = True
    DEBUG = True


