from core.memo import create_memo
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64

def generate_key(password):
    salt = b'salt_'  # You can change this salt value
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt(seed, password):
    key = generate_key(password)
    cipher_suite = Fernet(key)
    encrypted_seed = cipher_suite.encrypt(seed.encode())
    return encrypted_seed

def decrypt(encrypted_seed, password):
    key = generate_key(password)
    cipher_suite = Fernet(key)
    decrypted_seed = cipher_suite.decrypt(encrypted_seed).decode()
    return decrypted_seed


