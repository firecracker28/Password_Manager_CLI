import json
from auth import login,createLogin
from database import createVault,newEntry,remove,change,peek,find,create
import argparse
import sys
import os

 #TODO create arg parser
parser = argparse.ArgumentParser(prog ='main',allow_abbrev=False)
# Allows user only one action per session
parser.add_argument('--a',required=True)
parser.add_argument('--service')
parser.add_argument('--password')
parser.add_argument('--username')
parser.add_argument('--notes')


args = parser.parse_args()
if args.a == 'help':
    print('Usage: python3 main.py -a(action:add,delete,modify,search,view,generate,help) Optional: --service, --password, --username,--notes')
    sys.exit()
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
if data["hash"] == '':
    createLogin(input("Please create your master password: "))

access_granted = login(input("Please enter your master password: "))
if( not access_granted):
    print("Authentication failed please try again")
    sys.exit()

#creates table if not already created
createVault()

if args.a == 'add':
    newEntry(args.service,args.password,args.username,args.notes) 
elif args.a == 'delete':
    remove(args.service)
elif args.a== 'modify':
    change(args.service)
elif args.a == 'search':
    find(args.service)
elif args.a == 'view':
    peek(args.service)
elif args.a == 'generate':
    create()
else:
    print("Action given is not a valid action. Please try again")
    sys.exit()

