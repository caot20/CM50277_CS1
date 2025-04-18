import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'db', 'flights_management.db')
CREATE_TABLES_PATH = os.path.join(BASE_DIR, 'db', 'create_tables.sql')
DROP_TABLES_PATH = os.path.join(BASE_DIR, 'db', 'drop_tables.sql')
SEED_TABLES_PATH = os.path.join(BASE_DIR, 'db', 'seed_tables.sql')
