# Password_Manager
This is a Password Manager with a CLI interface that is created with Python. It uses security techniques like salts, hashing and encryption keys. All passwords are stored in an SQLite database.

## How it works
    1. Prompts user for master password or to create one for first time users. 
    2. Master is encrypted and hashed with salt
    3. If a user wants to create a new password or modify an existing one then a randomly generated encryption key is created and stored in memory
    4. After user ends session or timeout occurs encryption key is overwritten and deleted.

## more to come as I actually complete the project