import hashlib

def hash_password(pwd: str):
    return hashlib.sha256(pwd.encode("utf-8")).hexdigest()