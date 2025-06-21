import json
from auth import login,createLogin
from database import createVault
import argparse

try:
    with open('auth.json','r') as file:
        data = json.load(file)
except FileExistsError:
    print("auth.json not found, please contact support")

if not 'hash' in data:
    raise Exception("hash field not found, please contact support")

password = ""
if data["hash"] == '':
    password = input("Please create your master password")
    createLogin(password)
password = input("Please create your master password")
access_granted = login(password)
if( not access_granted):
    print("Authentication failed please try again")

createVault()
 #TODO create arg parser

