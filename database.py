import sqlite3

DATABASE = "trusttrail.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS producers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            location TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS batches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producer_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            quantity TEXT NOT NULL,
            origin TEXT NOT NULL,
            description TEXT,
            qr_file TEXT,
            status TEXT DEFAULT 'REGISTERED',
            FOREIGN KEY (producer_id) REFERENCES producers(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS deliveries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            batch_id INTEGER NOT NULL,
            amount TEXT NOT NULL,
            status TEXT DEFAULT 'PENDING',
            FOREIGN KEY (batch_id) REFERENCES batches(id)
        )
    """)

    connection.commit()
    connection.close()