import json
from auth import login,createLogin
import argparse
import sys
import pandas as pd
import cryptpandas as cp

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
    manager = pd.DataFrame(columns=['Service','Username','Password','Notes'])
else:
    access_granted = login(input("Please enter your master password: "))
    if( not access_granted):
        print("Authentication failed please try again")
        sys.exit()
    manager = cp.read_encrypted(path ='vault/vault.crypt',password=input("Please re-enter password to un-encrypt vault"))

if args.a == 'add':
    newColumn = pd.DataFrame({'Service':[args.service],'Username':[args.username],'Password':[args.password],'Notes':[args.notes]})
    manager = pd.concat([manager,newColumn], ignore_index=True)
    cp.to_encrypted(manager,password=input("please re-enter your password to encrypt vault:"),path = 'vault/vault.crypt')
elif args.a == 'delete':
    pass
elif args.a== 'modify':
    pass
elif args.a == 'search':
    pass
elif args.a == 'view':
    pass
elif args.a == 'generate':
    pass
else:
    print("Action given is not a valid action. Please try again")
    sys.exit()

