import json
from auth import login,createLogin,createKey
import argparse
import sys
import pandas as pd
import cryptpandas as cp
import random
from getpass import getpass
from cryptography.fernet import Fernet
import secrets
from cli import add,delete,modify,search,view,generate

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
    createLogin(getpass("Please create your master password: "))
    master = getpass("Please re-enter password to confirm: ")
    manager = pd.DataFrame(columns=['Service','Username','Password','Notes'])
else:
    master = getpass("Please enter your master password: ")
    if( not login(getpass("Please enter your master password: "))):
        print("Authentication failed please try again")
        sys.exit()
    manager = cp.read_encrypted(path ='vault/vault.crypt',password=master)

if args.a == 'add':
    manager = add(manager,args.service,args.password,args.username,args.notes)
elif args.a == 'delete':
    manager = delete(manager,args.service)
elif args.a == 'modify':
    manager = modify(manager,args.service,args.password,args.username,args.notes)
elif args.a == 'search':
    search(manager,args.service)
elif args.a == 'view':
    view(manager)
elif args.a == 'generate':
    generate()
else:
    print("Action given is not a valid action. Please try again")
cp.to_encrypted(manager,password=master,path = 'vault/vault.crypt')
master = secrets.token_hex(len(master))
del master

