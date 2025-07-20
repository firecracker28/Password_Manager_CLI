import json
from auth import login,createLogin,createKey,genPassword
import argparse
import sys
import pandas as pd
import cryptpandas as cp
import random
from getpass import getpass

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
    password = getpass("Please re-enter password to confirm: ")
    manager = pd.DataFrame(columns=['Service','Username','Password','Notes'])
else:
    password = getpass("Please enter your master password: ")
    if( not login(password)):
        print("Authentication failed please try again")
        sys.exit()
    manager = cp.read_encrypted(path ='vault/vault.crypt',password=password)

if args.a == 'add':
    newColumn = pd.DataFrame({'Service':[args.service],'Username':[args.username],'Password':[createKey(args.password)],'Notes':[args.notes]})
    manager = pd.concat([manager,newColumn], ignore_index=True)
    cp.to_encrypted(manager,password=password,path = 'vault/vault.crypt')
elif args.a == 'delete':
    print(manager)
    if args.service is not None:
        del_index = manager.index[manager['Service'] == args.service].to_list()
        manager = manager.drop(del_index[0])
    else:
        print("Please specify service of the password you wish to delete")
    cp.to_encrypted(manager,password=password,path = 'vault/vault.crypt')
    print(manager)
elif args.a== 'modify':
    if args.service is not None:
        mod_index = manager.index[manager['Service'] == args.service].to_list()
        if args.password is not None:
            manager.at[mod_index[0],createKey(args.password)]
        if args.username is not None:
            manager.at[mod_index[0],args.username]
        if args.notes is not None:
            manager.at[mod_index[0],args.notes]
    else:
        print("Please specify which service for which you wish to modify")
    cp.to_encrypted(manager,password=password,path = 'vault/vault.crypt')
elif args.a == 'search':
    pass
elif args.a == 'view':
    pass
elif args.a == 'generate':
    length = input("How long would you like your password to be: ")
    if length < 1 :
        print("Invalid password length")
        sys.exit()
    password = ''
    while(length > 0):
        rand_int = random.randint(33,125)
        password = password + chr(rand_int)
        length = length - 1
    print(password)
else:
    print("Action given is not a valid action. Please try again")
    sys.exit()
password = None
del password

