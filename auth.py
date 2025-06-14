import bcrypt
import json

#TODO add checks for all json read and writes
class Authentication:
    #creates hash for first time users
    def encrypt(password):
        salt = bcrypt.gensalt()
        bytes = password.encode("utf-8")
        hash = bcrypt.hashpw(bytes,salt)
        with open("auth.json","r") as existing_file:
            data = json.load(existing_file)

        data["hash"] = hash
        data["salt"] = salt

        with open("auth.json",'w') as updated_file:
            json.dumps(existing_file,updated_file,indent=4)
    
    def decrypt(password):
        bytes = password.encode("utf-8")
        with open("auth.json","r") as file:
            data = json.load(file)

        hash = data['hash']
        salt = data['salt']

        if(bcrypt.hashpw(bytes,salt) == hash):
            return True
        else:
            return False