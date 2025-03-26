from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

scrambled_message = []
enc_flag = ''

n = 0x1337
e = 0x10001

def find_cycles(perm):
    visited = set()
    cycles = []
    
    for i in range(len(perm)):
        if i not in visited:
            cycle = []
            j = i
            while j not in visited:
                visited.add(j)
                cycle.append(j)
                j = perm[j]
            
            cycles.append(cycle)
    
    return cycles

cycles = find_cycles(scrambled_message)

original_m = [0] * n

for cycle in cycles:
    k = len(cycle)
    d = pow(e, -1, k)
    
    for i in range(k):
        original_element = cycle[i]
        mapped_element = cycle[(i + d) % k]
        original_m[original_element] = mapped_element

key = sha256(str(original_m).encode()).digest()

cipher = AES.new(key, AES.MODE_ECB)
flag = cipher.decrypt(bytes.fromhex(enc_flag))
flag = unpad(flag, 16).decode()

print("Flag:", flag)