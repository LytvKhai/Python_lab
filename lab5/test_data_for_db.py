import sqlite3
from datetime import datetime, date, timedelta
from random import randint


def create_test_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    documents_data = [(i, f'document_{i}', datetime.now().date(),
                       randint(1, 15)) for i in range(1, 16)]
    users_data = [(i, f'user_{i}', f'position_{i + randint(1, 100)}',
                   randint(1, 15)) for i in range(1, 16)]
    departments_data = [(i, f'department №{i}', f'user_{16 - i}',
                         f'role_department_{16 - i}') for i in range(1, 16)]
    change_history_data = [(i, 16 - i, date(2023, 1, 1) + timedelta(days=i),
                            f'some change text №{i}') for i in range(1, 16)]

    cursor.executemany('INSERT INTO documents VALUES (?, ?, ?, ?)',
                       documents_data)
    cursor.executemany(f'INSERT INTO users VALUES (?, ?, ?, ?)', users_data)
    cursor.executemany(f'INSERT INTO departments VALUES (?, ?, ?, ?)',
                       departments_data)
    cursor.executemany(f'INSERT INTO change_history VALUES (?, ?, ?, ?)',
                       change_history_data)

    conn.commit()
