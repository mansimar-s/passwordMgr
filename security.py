import pickle
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


def maketest():
    d = {"a":"b", "c":"d"}
    fer = Fernet(make_ferKey("abcd"))
    token = fer.encrypt(pickle.dumps(d))
    with open("dict_temp.txt", "wb") as f:
        f.write(token)

"""

any hash stored in files needs to be encrypted by rsa

public key can be stored along with passict and private key can be the password
provided by the user

check online on standard method

"""

#maketest()



#changePass("abcd")
#key = Fernet.generate_key()
#f = Fernet(key)
#token = f.encrypt(b"secret")
#print(token)
#print(f.decrypt(token))
