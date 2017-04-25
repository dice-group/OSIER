import hashlib

def generate_id(byte_string):
    _hash = hashlib.md5()
    _hash.update(byte_string)
    hex_digest = _hash.hexdigest()
    return hex_digest
