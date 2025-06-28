import json
from auth import login,createLogin
from database import createVault,newEntry,remove,change,peek,find,create
import argparse
import sys

 #TODO create arg parser
parser = argparse.ArgumentParser(prog ='main',allow_abbrev=False)
# Allows user only one action per session
actions = parser.add_mutually_exclusive_group(required=True)
actions.add_argument('-a')
parser.add_argument('--service')
parser.add_argument('--password')
parser.add_argument('--username')
parser.add_argument('--notes')

args = parser.parse_args()
# checks prerequsites
try:
    with open('config/auth.json','r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("auth.json not found, please contact support")
    sys.exit()

if not 'hash' in data:
    raise Exception("hash field not found, please contact support")

#Determines if user is returning or new
password = ""
if data["hash"] == '':
    password = input("Please create your master password")
    createLogin(password)
password = input("Please enter your master password")
access_granted = login(password)
if( not access_granted):
    print("Authentication failed please try again")
    sys.exit()

#creates table if not already created
createVault()

if args.a == 'add':
    newEntry(args.service,args.password,args.username,args.notes)
elif args.delete == 'delete':
    remove(args.service)
elif args.modify == 'modify':
    change(args.service)
elif args.search == 'search':
    find(args.service)
elif args.view == 'view':
    peek(args.service)
elif args.generate == 'generate':
    create()
else:
    print("Action given is not a valid action. Please try again")
    sys.exit()

