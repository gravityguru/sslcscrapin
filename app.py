import requests
from bs4 import BeautifulSoup

login_data = {
    'username':"1ms17ee066",
    'password':'23-09-1999',
    'submit.x':18,
    'submit.y':17,
    'option': 'com_user',
    'task': 'login'
}

with requests.Session() as s:
    url= "http://parents.msrit.edu"
    r = s.get(url)
    print(r.content)
    soup = BeautifulSoup(r.content, "html.parser")
    r = s.post(url,data=login_data)
    print(r.content)
