# Password_Manager
This is a Password Manager with a CLI interface that is created with Python. It uses security techniques like salts, hashing and encryption keys.

## How it works
    1. User picks from 7 avaliable actions
        1. help - gives user list of possible actions
        2. add - adds password to password manager
        3. delete- deletes password from password manager
        4. search - user can search for a specific password by service name
        5. modify - user can modify any entry in the password manager
        6. view - user can view every entry in the password manager
        7. generate - generates a strong password of any length for user.
    2. Prompts user for master password or creates one for first time users.  Also a Dataframe is created and stored in vault/vault.crypt if it does not already exist. Master password is stored so that dataframe can be encrypted.
    3. Master password is hashed with a randomly generated salt using bcrypt and stored in config/auth.json
    4. User chooses an action from list in step 1.
    5. Once action has been completed the program exists

## Features to Add
    1. Allow user to complete multiple actions in one session
    2. Build out the UI(Details still unknown)
    3. Add some more checks and security features