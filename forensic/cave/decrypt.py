import base64

key1 = base64.b64decode("NXhzR09iakhRaVBBR2R6TGdCRWVJOHUwWVNKcTc2RWl5dWY4d0FSUzdxYnRQNG50UVk1MHlIOGR6S1plQ0FzWg==").decode('utf-8')
key2 = base64.b64decode("n2mmXaWy5pL4kpNWr7bcgEKxMeUx50MJ").decode('utf-8', errors='replace')

def decrypt_file(encrypted_file_path, output_file_path):
    with open(encrypted_file_path, 'rb') as f:
        encrypted_b64 = f.read().decode('utf-8').strip() 

    encrypted_bytes = base64.b64decode(encrypted_b64)

    print(f"First 16 bytes: {encrypted_bytes[:16].hex()}")
    
    key1_bytes = key1.encode('utf-8')
    key2_bytes = key2.encode('utf-8')

    decrypted_bytes = bytearray()
    
    for i in range(len(encrypted_bytes)):
        k1 = key1_bytes[i % len(key1_bytes)]
        k2 = key2_bytes[i % len(key2_bytes)]
        decrypted_byte = encrypted_bytes[i] ^ k1 ^ k2
        decrypted_bytes.append(decrypted_byte)

    if decrypted_bytes.startswith(b'%PDF'):
        print("PDF header detected - decryption likely successful!")
    else:
        print("Warning: PDF header not found - decryption may have failed")
        print(f"First 16 decrypted bytes: {decrypted_bytes[:16]}")
    
    with open(output_file_path, 'wb') as f:
        f.write(decrypted_bytes)

def main():
    enc_file_path = "map.pdf.secured"
    denc_file_path = "map_restored.pdf"
    decrypt_file(enc_file_path, denc_file_path)

if __name__ == '__main__':
    main()
