import os
import random
import time
import base64


def encrypt_binary(input_file: str, output_file: str, key_file: str):
    with open(input_file, "rb") as file:
        data = file.read()
    key = random.randbytes(len(data))
    with open(key_file, "wb") as file:
        file.write(key)
    encrypted = bytes([b ^ k for b, k in zip(data, key)])
    with open(output_file, "wb") as file:
        file.write(encrypted)


def decrypt_binary(encrypted_file: str, output_file: str, key_file: str):
    with open(encrypted_file, "rb") as file:
        encrypted_data = file.read()
    with open(key_file, "rb") as file:
        key = file.read()
    decrypted = bytes([e ^ k for e, k in zip(encrypted_data, key)])
    with open(output_file, "wb") as file:
        file.write(decrypted)


# 11. XOR titkosítás 2MB+ bináris állománnyal
def large_file_encryption(input_file: str, encrypted_file: str, key_file: str):
    with open(input_file, "rb") as file:
        data = file.read()
    key = random.randbytes(len(data))
    encrypted = bytes([b ^ k for b, k in zip(data, key)])
    with open(encrypted_file, "wb") as file:
        file.write(encrypted)
    with open(key_file, "w") as file:
        file.write(base64.b64encode(key).decode())


if __name__ == "__main__":
    # large_file_encryption("large_input.bin", "large_encrypted.bin", "key.txt")
    encrypt_binary("input.jpg", "output.jpg", "key.txt")
    decrypt_binary("output.jpg", "decrypted.jpg", "key.txt")
