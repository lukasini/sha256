import hashlib

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
sex = input("Insert text to be converted into hash:")
hash_string = sex
sha_signature = encrypt_string(hash_string)
print(sha_signature)
