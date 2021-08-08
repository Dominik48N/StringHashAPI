import base64
import hashlib
import bcrypt


def create_string_hash(string: str):
    string = string.encode("utf-8")
    string = base64.b64encode(hashlib.sha256(string).digest())
    hashed = bcrypt.hashpw(
        string,
        bcrypt.gensalt(12)
    )
    return hashed.decode()


def check_string_hash(string: str, hash_value: str):
    string = string.encode("utf-8")
    string = base64.b64encode(hashlib.sha256(string).digest())
    hash_value = hash_value.encode("utf-8")

    if bcrypt.checkpw(string, hash_value):
        return True
    else:
        return False
