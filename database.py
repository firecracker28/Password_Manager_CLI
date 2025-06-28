import sqlite3
from auth import createKey

def createVault():
    try:
        with sqlite3.connect("database/passwords.db") as conn:
            print("Database opened")
            conn.execute("PRAGMA journal_mode=WAL;")
            create_table_statement = """CREATE TABLE IF NOT EXISTS manager (
            id INTEGER PRIMARY KEY,
            username TEXT,
            encryptionKey TEXT NOT NULL,
            service TEXT,
            notes TEXT
            );"""
            cursor = conn.cursor()
            print("Creating table")
            cursor.execute(create_table_statement)
            conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Error in connection to the database: {e}")

def newEntry(service,password,username,notes):
    key = createKey(password)
    add_statement = """INSERT INTO manager (username, encryptionKey, service, notes)
    VALUES (?, ?, ?, ?)
    """
    try:
        with sqlite3.connect("database/passwords.db") as conn:
            print("Database opened")
            conn.execute("PRAGMA journal_mode=WAL;")
            cursor = conn.cursor()
            cursor.execute(add_statement,(username,key,service,notes))
            conn.commit()

    except sqlite3.OperationalError as e:
        print(f"Error in connection to the database: {e}")

def remove(service):
    pass

def change (service):
    pass

def peek (service):
    pass

def create():
    pass

def find(service):
    pass
    
