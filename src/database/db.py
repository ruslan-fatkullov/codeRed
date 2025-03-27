import sqlite3


# Функция для инициализации базы данных и создания таблицы
def init_db(database):
    print("init db")
    # Создание или подключение к базе данных
    conn = sqlite3.connect(database)

    # Создание курсора
    c = conn.cursor()

    # Создание таблицы Content
    c.execute('''CREATE TABLE IF NOT EXISTS service (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT,
                 service_type INTEGER,
                 description TEXT,
                 price TEXT,
                 dev_time TEXT,
                 route TEXT,
                 big_image TEXT,
                 icon TEXT,
                 published BOOLEAN)''')

    c.execute('''CREATE TABLE IF NOT EXISTS service_feature (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 feature_text TEXT,
                 feature_img TEXT,
                 altitude_img TEXT,
                 service_id INTEGER,
                 FOREIGN KEY (service_id) REFERENCES service(id)
                 )''')

    # Создание таблицы Users
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT,
                 password TEXT)''')

    # Закрытие соединения с базой данных
    conn.close()
