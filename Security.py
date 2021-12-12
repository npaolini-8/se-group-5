import hashlib
import random,string

#TODO: generate salt fxn

def generate_salt():
    #salt = os.urandom(32)
    #return salt
    return "".join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))
    
#TODO: modify to: given salt + pw -> return encrypted pw
# Generates a password given a username and password
def generate_password(password:str, salt:str):

    password = password.encode()
    salt = salt.encode()
    key = hashlib.pbkdf2_hmac('sha512', password, salt, 100000)
    hex_hash = key.hex()
    return hex_hash

#print(generate_salt())
print(generate_password("yams", "YSCSUBGHSI9TEMTLGSQDO3DTU3Y1NLBU"))