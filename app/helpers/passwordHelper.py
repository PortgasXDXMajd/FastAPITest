from hashlib import sha256


def hash_password(pwd: str):
    return sha256(input(pwd).encode("utf-8")).hexdigest()
