import os


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT'))
    MAIL_USE_TLS = bool(int(os.environ.get('MAIL_USE_TLS')))
    MAIL_USE_SSL = bool(int(os.environ.get('MAIL_USE_SSL')))
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')

    QUESTIONS_PER_PAGE = 10
    ANSWERS_PER_PAGE = 10


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://flaskuser:qwerty@localhost/flaskaskdb'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://flaskuser:qwerty@localhost/flaskaskdb_prod'


config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig
}
