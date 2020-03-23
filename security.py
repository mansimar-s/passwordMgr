import pickle
from cryptography.fernet import Fernet
import hashlib, base64

def myHash(s):
    m = hashlib.new("sha256")
    m.update(bytes(s,'utf-8'))
    return bytes(m.hexdigest(),'utf-8')



def changePass(s):

    """
    Used for changing the password"
    """
    make_ferKey(s) # It is really important to call this function here
                   # I think it ensures the data is encrypted by the current
                   # password as the token and not the old password
    with open('mysec.txt', 'rb+') as f:
        f.seek(0)
        f.truncate()
        f.seek(0)
        f.write(myHash(s))

def make_ferKey(s):

    """
    I dont konw exactly what this function does now
    All I know is it is important to call it with the password once
    so that the data is encrypted by the current password as its token.
    """

    #print("Interacting with make ferKey")

    key = hashlib.md5(bytes(s, 'utf-8')).hexdigest()
    key64 = base64.urlsafe_b64encode(bytes(str(key), 'utf-8'))
    return key64


def maketest():

    """
    This is just a test function I used while initial development!
    Dont play around with this as even I cant understand what I did
    with all the crazy cryptography
    """

    #print("Interacting with maketest")

    #d = {"a":"b", "c":"d"}
    d = {"a":"b", "c":"d", "e" : "f"}
    #fer = Fernet(make_ferKey("abcd"))
    fer = Fernet(make_ferKey("abcdef"))
    token = fer.encrypt(pickle.dumps(d))
    with open("mysec.txt", "wb") as f:
        f.write(token)

"""

any hash stored in files needs to be encrypted by rsa

public key can be stored along with passict and private key can be the password
provided by the user

check online on standard method

"""

#maketest()



#changePass("abcdef")
#key = Fernet.generate_key()
#f = Fernet(key)
#token = f.encrypt(b"secret")
#print(token)
#print(f.decrypt(token))
