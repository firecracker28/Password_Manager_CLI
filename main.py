import json
from auth import encrypt,decrypt

try:
    with open('auth.json','r') as file:
        data = json.load(file)
except FileExistsError:
    print("auth.json not found, please contact support")

if not 'hash' in data:
    raise Exception("hash field not found, please contact support")

password = ""
if data["hash"] != '':
    password = input("Please enter the master password")
    access_granted = decrypt(password)
    if( not access_granted):
        print("Authentication failed please try again")
else:
    password = input("Please create your master password")
    encrypt(password)