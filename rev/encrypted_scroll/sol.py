msg = "IUC|t2nqm4`gm5h`5s2uin4u2d~"

def apply_shift(msg):
    return ''.join(chr(ord(c) - 1) for c in msg)

decrypted_msg = apply_shift(msg)

print(decrypted_msg)