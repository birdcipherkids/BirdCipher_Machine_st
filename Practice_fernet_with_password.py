import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt_with_fernet(salt, password, pass_app):

#password = b"Birdcipher666"
# salt = os.urandom(16)
# print(salt)
# base64_string = base64.b64encode(salt).decode('ascii')
# print(base64_string)

    #salt1 = base64.b64decode(salt)
    #print(salt1)
    password = password.encode()
    pass_app = pass_app.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    print(key)
    f = Fernet(key)
    token = f.encrypt(pass_app)
    print(token)

    text = f.decrypt(token)
    print(text)

    return token


# password = 'Birdcipher666'
# salt = '6iIcZHONiYqIqAs11iQtSQ=='
# pass_app = 'tujmONjNYxYzARQ28xJYOKY8R0ln07'
# token_s = encrypt_with_fernet(salt, password, pass_app)
# print(token_s)








# text = f.decrypt(token)
# print(text)
