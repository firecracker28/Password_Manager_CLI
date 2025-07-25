import pandas as pd
import random
import sys
import cryptography.fernet as Fernet
import json

class Cli:
    def add(manager,service,password,username,notes):
        newColumn = pd.DataFrame({'Service':[service],'Username':[username],'Password':[password],'Notes':[notes]})
        if len(manager.index[manager['Service'] == service]) == 0:
            manager = pd.concat([manager,newColumn], ignore_index=True)
        else:
            print(f'A password for {service} already exists. Please use modify if you wish to change it.')
        return manager
    def delete(manager,service):
        if service is not None:
            del_index = manager.index[manager['Service'] == service].to_list()
            if del_index:
                manager = manager.drop(del_index[0])
            else:
                print("Service not found, please try again")
        else:
            print("Please specify service of the password you wish to delete")
        return manager
    def modify(manager,service,password,username,notes):
        if service is not None:
            mod_index = manager.index[manager['Service'] == service].to_list()
            if mod_index:
                if username is not None:
                    manager.at[mod_index[0],'Username'] = username
                if password is not None:
                    manager.at[mod_index[0],'Password'] = password
                if notes is not None:
                    manager.at[mod_index[0],'Notes'] = notes
            else:
                print("entry not found,please try again")
        else:
            print("Please specify which service for which you wish to modify")
        return manager
    def generate():
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
    def search(manager,service):
        row_retrevied = manager.index[manager['Service'] == service].to_list()
        if row_retrevied:
            print(manager.iloc[row_retrevied[0]])
            reveal_pass = input("Do you wish to view your password?(y/n)")
            if reveal_pass.lower() == 'y':
                with open("config/auth.json",'r') as key_file:
                    key = json.load(key_file)
                cipher = Fernet(key['key'].encode())
                print(cipher.decrypt(manager.at[row_retrevied[0],'Password']).decode())
        else:
            print('Service not found,please try again')
    def view(manager):
        for index,row in manager.iterrows():
            print(f"Service: {row['Service']}, Username: {row['Username']}, Password: use search to see password, Notes: {row['Notes']}")