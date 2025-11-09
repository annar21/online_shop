from sqlite3 import connect, Row
from config import Config

def get_db():
    conn = connect(Config.DB_NAME)
    conn.row_factory = Row

    return conn

def init_db():
    db = get_db() 
    cursor = db.cursor()

    # init tables
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS sellers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50) NOT NULL UNIQUE               
        );
    """)