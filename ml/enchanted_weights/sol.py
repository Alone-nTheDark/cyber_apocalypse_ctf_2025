import torch

checkpoint = torch.load('eldorian_artifact.pth')

hidden_weights = checkpoint['hidden.weight']

diagonal_values = hidden_weights.diagonal()

flag = ''.join(chr(int(val)) for val in diagonal_values if 32 <= val <= 126)

print("Flag:", flag)
