from cryptography.fernet import Fernet
import hashlib

def myHash(s):
    m = hashlib.new("sha256")
    m.update(("%s" % s).encode('utf-8'))
    return m.hexdigest()


def changePass(s):
    with open('mysec.txt', 'r+') as f:
        f.seek(0)
        f.truncate()
        f.seek(0)
        f.write(myHash(s))

def encrypt():
    """
    Takes the pickled password database and encrypts it using fernet method.
    Will require reading the AES key.
    """
    pass


def decrypt():
    pass


key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"secret")
print(token)
print(f.decrypt(token))
