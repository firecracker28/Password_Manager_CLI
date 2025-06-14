import json
from auth import encrypt,decrypt

#TODO add checks for empty file and if hash doesn't exist
with open('auth.json','r') as file:
    data = json.load(file)

password = ""
if data["hash"] != '':
    password = input("Please enter the master password")
    access_granted = decrypt(password)
    if( not access_granted):
        print("Authentication failed please try again")
else:
    password = input("Please create your master password")
    encrypt(password)