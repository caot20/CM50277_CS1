import sqlite3
from config import settings

def get_connection():
    return sqlite3.connect(settings.DB_PATH)

def create_tables():
    with open(settings.CREATE_TABLES_PATH, 'r') as f:
        db_create_tables = f.read()

    with get_connection() as db_connection:
        db_connection.executescript(db_create_tables)

def drop_tables():
    with open(settings.DROP_TABLES_PATH, 'r') as f:
        db_drop_tables = f.read()

    with get_connection() as db_connection:
        db_connection.executescript(db_drop_tables)

def seed_tables():
    """
    """
    with open(settings.SEED_TABLES_PATH, 'r') as f:
        db_seed_tables = f.read()

    with get_connection() as db_connection:
        db_connection.executescript(db_seed_tables)            
   
