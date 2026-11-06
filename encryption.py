
import os
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


def generate_key(password, salt):
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1
    )
    return kdf.derive(password.encode())


def encrypt_message(message, password):
    salt = os.urandom(16)
    nonce = os.urandom(12)

    key = generate_key(password, salt)
    aes = AESGCM(key)

    ciphertext = aes.encrypt(
        nonce,
        message.encode(),
        None
    )

    result = salt + nonce + ciphertext

    return base64.b64encode(result).decode()
