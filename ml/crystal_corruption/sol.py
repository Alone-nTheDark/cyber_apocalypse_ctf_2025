import pickletools
import struct
import zipfile
import numpy as np
import torch
import pickletools

model_path = 'resnet18.pth'

with zipfile.ZipFile(model_path, 'r') as zip_ref:
    if 'resnet18/data.pkl' in zip_ref.namelist():
        with zip_ref.open('resnet18/data.pkl') as pkl_file:
            data = pkl_file.read()
            
            pickletools.dis(data)

def stego_decode(tensor, n=3):
    bits = np.unpackbits(tensor.numpy().view(np.uint8))

    payload = np.packbits(np.concatenate([np.vstack(tuple([bits[i::tensor.dtype.itemsize * 8] for i in range(8 - n, 8)]))
                                          .ravel("F")])).tobytes()

    size, checksum = struct.unpack("i 64s", payload[:68])
    message = payload[68:68+size]
    
    return message


model = torch.load(model_path, weights_only=False)

for name, tensor in model.items():
    try:
        payload = stego_decode(tensor) 
        print(payload)
    except:
        break