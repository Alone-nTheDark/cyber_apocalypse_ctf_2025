import base64

string = "LmB9ZDNsNDN2M3JfYzFnNG1fM251cntCVEhgIHNpIGxsZXBzIHRlcmNlcyBlaFQ="

decoded = base64.b64decode(string).decode('utf-8')
start_index = decoded.find("`") + 1
end_index = decoded.find("`", start_index)
decoded = decoded[start_index:end_index]

print(decoded[::-1])