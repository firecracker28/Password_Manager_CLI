import sqlite3

try:
    with sqlite3.connect("passwords.db") as conn:
        print("Database opened")

except sqlite3.OperationalError as e:
    print(f"Error in connection to the database: {e}")