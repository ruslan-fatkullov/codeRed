import sqlite3


def create_service(database, title, service_type, description, price, dev_time, route, big_image, icon, published):
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()

        c.execute(
            'INSERT INTO service '
            '(title, service_type, description, price, dev_time, route, big_image, icon, published) '
            'VALUES '
            '(?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (title, service_type, description, price, dev_time, route, big_image, icon, published))

        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def update_service(database, title, service_type, description, price, dev_time, route, big_image, icon, published, service_id):
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()

        c.execute(
            'UPDATE service SET '
            'title=?, '
            'service_type=?, '
            'description=?, '
            'price=?, '
            'dev_time=?, '
            'route=?, '
            'big_image=?, '
            'icon=?,'
            'published=?'
            'WHERE id=?',
            (title, service_type, description, price, dev_time, route, big_image, icon, published, service_id))

        conn.commit()
        conn.close()
    except Exception as e:
        print("here")
        print(e)


def get_service_by_id(database, service_id):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('SELECT * FROM service WHERE id = ?', (service_id,))
    result = c.fetchone()
    conn.commit()
    conn.close()
    if result:
        return result


def get_all_service(database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('SELECT * FROM service')
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows


def get_limit_random_service(database, limit):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('SELECT * FROM service ORDER BY RANDOM() LIMIT ?', (limit,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete_service_by_id(database, service_id):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('DELETE FROM service WHERE id=(?)', (service_id,))
    conn.commit()
    conn.close()


def get_service_by_type(database, service_type):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('SELECT title, route FROM service WHERE service_type=(?)', (service_type,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows


def get_service_by_route(database, value):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('SELECT * FROM service WHERE route=?', (value,))
    result = c.fetchone()
    conn.commit()
    conn.close()
    if result:
        return result
