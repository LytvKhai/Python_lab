import sqlite3

# Класс кольорів, для зміни кольору виводу у термінал
class Colors:
    DEFAULT = '\033[0m'
    CHANGED = '\033[95m'

# Тестові запити
def test_requests():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()
    # Простий запит с однієї таблиці
    print(f'{Colors.CHANGED}Simple request:')
    simple_response = cursor.execute('''
        SELECT name_document, create_date FROM documents;
    ''').fetchall()
    print_response(simple_response)
    # Перекресний запит
    print(f'{Colors.CHANGED}Cross join request:')
    cross_join = cursor.execute("""
        SELECT documents.name_document, users.name
        FROM documents INNER JOIN users
        ON documents.user = users.id_user;
    """)
    print_response(cross_join)
    # Запит зі всіма таблицями
    print(f'{Colors.CHANGED}Using different tables request:')
    using_different_tables = cursor.execute('''
        SELECT documents.name_document,
        users.name, departments.name_department,
        change_history.change_date
        FROM documents
        JOIN users ON documents.user = users.id_user
        JOIN departments ON users.id_department = departments.id_department
        JOIN change_history ON change_history.id_document = documents.id_document;
    ''')
    print_response(using_different_tables)
    # Запит с прорахунками
    print(f'{Colors.CHANGED}aggregated characteristics request:')
    aggregated_characteristics = cursor.execute('''
    SELECT documents.name_document, change_history.change_date
    FROM documents
    LEFT JOIN change_history ON documents.id_document = change_history.id_document
    WHERE change_history.change_date > '2023-01-05';
    ''')
    print_response(aggregated_characteristics)
    conn.close()

# Вивід відповіді
def print_response(obj):
    for line in obj:
        print(f'{Colors.DEFAULT}', line)
