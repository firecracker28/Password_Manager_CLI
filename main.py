import json
from auth import login,createLogin
from database import createVault,newEntry,remove,change,peek,find,create
import argparse
import sys

 #TODO create arg parser
parser = argparse.ArgumentParser(prog ='main',allow_abbrev=False)
# Allows user only one action per session
actions = parser.add_mutually_exclusive_group('Actions:',required=True)
actions.add_argument('-a','add')
actions.add_argument('-d','delete')
actions.add_argument('-m', 'modify')
actions.add_argument('-s', 'search')
actions.add_argument('-v','view')
actions.add_argument('-g', 'generate')
parser.add_argument('--service')
parser.add_argument('--password')
parser.add_argument('--username')
parser.add_argument('--notes')

args = parser.parse_args()
# checks prerequsites
try:
    with open('auth.json','r') as file:
        data = json.load(file)
except FileExistsError:
    print("auth.json not found, please contact support")

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

if args.add is not None:
    newEntry(args.service,args.password,args.username,args.notes)
elif args.delete is not None:
    remove(args.service)
elif args.modify is not None:
    change(args.service)
elif args.search is not None:
    find(args.service)
elif args.view is not None:
    peek(args.service)
elif args.generate is not None:
    create()
else:
    print("No valid arguments given, please try again")
    sys.exit()

