class Config(object):
    """
    Common configurations
    """
    import os
    SECRET_KEY = os.urandom(32)
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI='sqlite:///EmployeeData.db'
    # SQLALCHEMY_DATABASE_URI=''
    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    # setting this to True activates the debug mode on the app.
    # This allows us to use the Flask debugger in case of an unhandled exception, and
    # also automatically reloads the application when it is updated.
    SQLALCHEMY_ECHO = True
    # setting this to True helps us with debugging by allowing SQLAlchemy to
    # log errors.


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
