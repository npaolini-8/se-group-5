import os
import hashlib

class password():
    
    # Generates a password given a username and password
    def generate_password(username, password):

        users = {}
        salt = os.urandom(32)
        plaintext = 'password'.encode()
    
        key = hashlib.pbkdf2_hmac('sha512', plaintext, salt, 100000)
        hex_hash = key.hex()
        users[username] = {'salt' : salt, 'key' : key}

    # Checks to see if a the new hash of a password is the same as the original
    def check_password(self, username, password, salt):

        # Checking to see if the orignal key is the same as the old key
        salt = self.users[username]['salt']
        key = self.users[username]['key']
        new_hex = hashlib.pbkdf2_hmac('sha512', self.plaintext, salt, 100000)

        if self.hex_hash == new_hex:
            return True
        else:
            return False