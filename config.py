import os


class Config:
    # Секретный ключ для защиты от CSRF атак и других целей
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sdijbngdfgdfkgv bfdsl'

    # Папка для загрузки файлов
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'uploads'

    # Разрешенные расширения файлов
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'svg', 'webp'}


    # Настройки базы данных
    DATABASE = 'code_red.db'
    #     {
    #     'name': os.environ.get('DATABASE_NAME') or 'app.db',
    #     'engine': 'peewee.SqliteDatabase',
    #     'user': os.environ.get('DATABASE_USER') or '',
    #     'password': os.environ.get('DATABASE_PASSWORD') or '',
    #     'host': os.environ.get('DATABASE_HOST') or 'localhost',
    #     'port': os.environ.get('DATABASE_PORT') or 3306
    # }


# Вы можете создать дополнительные классы для разных конфигураций, например, для разработки, тестирования и производства
class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DATABASE = {
        'name': 'test.db',
        'engine': 'peewee.SqliteDatabase',
    }


class ProductionConfig(Config):
    DEBUG = False


# Словарь для удобного выбора конфигурации
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
