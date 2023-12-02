import database
import test_data_for_db
import test_request

# Запуск методів
database.create_db()
test_data_for_db.create_test_data()
test_request.test_requests()
