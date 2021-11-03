import os
import hashlib

def security(username, password):

    users = {}
    
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    users[username] = {'salt' : salt, 'key' : key}

    # Checking to see if the orignal key is the same as the old key
    salt = users[username]['salt']
    key = users[username]['key']
    new_key = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)

    assert key == new_key

    

