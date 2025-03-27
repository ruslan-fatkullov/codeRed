import sqlite3
import hashlib


def create_user(database, username, password):
    # Хеширование пароля
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Подключение к нашей базе данных
    conn = sqlite3.connect(database)
    c = conn.cursor()

    # Добавление нового пользователя
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

    # Сохранение изменений и закрытие соединения с базой данных
    conn.commit()
    conn.close()


