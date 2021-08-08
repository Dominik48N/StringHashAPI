import bcrypt


def create_string_hash(string: str):
    string = string.encode("utf-8")
    hashed = bcrypt.hashpw(
        string,
        bcrypt.gensalt(12)
    )
    return hashed.decode()