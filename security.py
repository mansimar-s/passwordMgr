from cryptography.fernet import Fernet
import hashlib, base64

def myHash(s):
    m = hashlib.new("sha256")
    m.update(bytes(s,'utf-8'))
    return bytes(m.hexdigest(),'utf-8')



def changePass(s):
    with open('mysec.txt', 'rb+') as f:
        f.seek(0)
        f.truncate()
        f.seek(0)
        f.write(myHash(s))

def make_ferKey(s):
    key = hashlib.md5(bytes(s, 'utf-8')).hexdigest()
    key64 = base64.urlsafe_b64encode(bytes(str(key), 'utf-8'))
    return key64






"""
Have to make a temporary dict, pickle it, encrypt it using the same fernet
and write it to dict_temp.txt
Then in main.py it will be decrypted by the source code
"""




def encrypt():
    """
    Takes the pickled password database and encrypts it using fernet method.
    Will require reading the AES key.
    """
    pass


def decrypt():
    pass




#changePass("abcd")
#key = Fernet.generate_key()
#f = Fernet(key)
#token = f.encrypt(b"secret")
#print(token)
#print(f.decrypt(token))
