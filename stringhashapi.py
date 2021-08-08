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