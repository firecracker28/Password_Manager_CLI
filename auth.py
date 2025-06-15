import bcrypt
import json

#TODO add checks for all json read and writes
class Authentication:
    #creates hash for first time users
    def encrypt(password):
        salt = bcrypt.gensalt()
        bytes = password.encode("utf-8")
        hash = bcrypt.hashpw(bytes,salt)
        try:
            with open("auth.json","r") as existing_file:
                data = json.load(existing_file)
        except Exception as e:
            print(f"an unexpected error has occured:,{e}")

        data["hash"] = hash
        data["salt"] = salt

        try:
            with open("auth.json","r") as existing_file:
                data = json.load(existing_file)
        except Exception as e:
            print(f"an unexpected error has occured:,{e}")
    
    def decrypt(password):
        bytes = password.encode("utf-8")
        try:
            with open("auth.json","r") as existing_file:
                data = json.load(existing_file)
        except Exception as e:
            print(f"an unexpected error has occured:,{e}")

        hash = data['hash']
        salt = data['salt']

        if(bcrypt.hashpw(bytes,salt) == hash):
            return True
        else:
            return False