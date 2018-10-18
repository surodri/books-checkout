import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
     
    @staticmethod
    def init_app(app):
        pass


class Config_Test(object):

    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASEDIR, 'test/test_database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TESTING = True
    DEBUG = True

    @staticmethod
    def init_app(app):
         pass
