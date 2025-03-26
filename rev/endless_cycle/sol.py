encrypted_flag = bytes.fromhex("b6 9e ad c5 92 fa df d5 a1 a8 dc c7 ce a4 8b e1 8a a2 dc e1 89 fa 9d d2 9a b7")
xor_key = 0xbeefcafe

def rotate_key(key):
    return (key >> 8) | ((key & 0xFF) << 24)

decrypted_flag = bytes(byte ^ (xor_key & 0xFF) for byte in encrypted_flag)

for _ in encrypted_flag:
    xor_key = rotate_key(xor_key)

print("Flag:", decrypted_flag.decode())
