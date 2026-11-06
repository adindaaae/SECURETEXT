
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from encryption import generate_key


def decrypt_message(encrypted_message, password):
    try:
        data = base64.b64decode(
            encrypted_message,
            validate=True
        )

        if len(data) < 44:
            raise ValueError("Data enkripsi tidak valid")

        salt = data[:16]
        nonce = data[16:28]
        ciphertext = data[28:]

        key = generate_key(password, salt)
        aes = AESGCM(key)

        plaintext = aes.decrypt(
            nonce,
            ciphertext,
            None
        )

        return plaintext.decode("utf-8")

    except Exception:
        raise ValueError(
            "Dekripsi gagal! Password salah atau data rusak."
        )
