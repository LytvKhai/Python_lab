import sqlite3


def create_db():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS documents;''')
    cursor.execute('''DROP TABLE IF EXISTS users;''')
    cursor.execute('''DROP TABLE IF EXISTS departments;''')
    cursor.execute('''DROP TABLE IF EXISTS change_history;''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
            id_document INT PRIMARY KEY,
            name_document TEXT,
            create_date DATE,
            user INT,
            FOREIGN KEY (user) REFERENCES users (id_user)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
            id_user INT PRIMARY KEY,
            name TEXT,
            position TEXT,
            id_department INT,
            FOREIGN KEY (id_department) REFERENCES departments (id_department)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
            id_department INT PRIMARY KEY,
            name_department TEXT,
            head_of_department INT,
            role_department TEXT,
            FOREIGN KEY (head_of_department) REFERENCES users (id_user)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS change_history (
            id_change INTEGER PRIMARY KEY,
            id_document INT,
            change_date DATE,
            text_change TEXT,
            FOREIGN KEY (id_document) REFERENCES documents (id_document)
    );
    ''')

    conn.commit()
    conn.close()
