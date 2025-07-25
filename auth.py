import bcrypt
import json
import sys
import random
from cryptography.fernet import Fernet

    #creates hash for first time users
def createLogin(password):
    salt = bcrypt.gensalt()
    bytes = password.encode("utf-8")
    hash = bcrypt.hashpw(bytes,salt)
    with open("config/auth.json","r") as existing_file:
        data = json.load(existing_file)
    data['hash'] = hash.decode("utf-8")
    data['salt'] = salt.decode("utf-8")
    with open("config/auth.json","w") as existing_file:
        json.dump(data,existing_file,indent=4)
    
def login(password):
    bytes = password.encode("utf-8")
    try:
        with open("config/auth.json","r") as existing_file:
            data = json.load(existing_file)
    except Exception as e:
        print(f"an unexpected error has occured:,{e}")

    hash = data['hash'].encode("utf-8")
    salt = data['salt'].encode("utf-8")

    if(bcrypt.hashpw(bytes,salt) == hash):
        return True
    else:
        return False
    
def createKey(password):
    with open("config/auth.json","r") as existing_file:
        data = json.load(existing_file)

    if data['key'] == '':
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted = cipher.encrypt(password.encode())
        data['key'] = key.decode("utf-8")
        with open("config/auth.json","w") as existing_file:
            json.dump(data,existing_file,indent=4)
    else:
        cipher = Fernet(data['key'].encode())
        encrypted = cipher.encrypt(password.encode())
    
    return encrypted
def genPassword(length):
    if length < 1 :
        print("Invalid password length")
        sys.exit()
    password = ''
    while(length > 0):
        rand_int = random.randint(33,125)
        password = password + chr(rand_int)
        length = length - 1
    return password