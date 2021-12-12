import os
import hashlib

class password():

    #TODO: generate salt fxn

    def generate_salt(self):
        salt = os.urandom(32)
        return salt
        
    #TODO: modify to: given salt + pw -> return encrypted pw
    # Generates a password given a username and password
    def generate_password(self,username, password, salt):

        plaintext = 'password'.encode()
        key = hashlib.pbkdf2_hmac('sha512', plaintext, self.salt, 100000)
        hex_hash = key.hex()
        return hex_hash

#pw = password()
#new_password = pw.generate_salt()
#pw.generate_password("someuser","somepw", new_password)