import sqlite3

def createVault():
    try:
        with sqlite3.connect("passwords.db") as conn:
            print("Database opened")

    except sqlite3.OperationalError as e:
        print(f"Error in connection to the database: {e}")
    create_table_statement = """CREATE TABLE IF NOT EXISTS manager
    id INT NOT NULL,
    username TEXT,
    encryptionKey TEXT NOT NULL,
    service TEXT,
    notes TEXT"
    cursor = conn.cursor()
    print("Creating table")
    cursor.execute(create_table_statement)
    conn.commit()
    conn.close()
    print("Database closed")"""

def newEntry(service,password,username,notes):
    pass

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
    
