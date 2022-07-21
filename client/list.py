from email import header
import requests
from getpass import getpass

auth_endpoint="http://localhost:8000/api/products/"
password=getpass()

auth_response=requests.post(auth_endpoint,json={'username':'user','password':password})
print(auth_response.json())

if auth_response.status_code==200:
    token=auth_response.json()['token']
    header={
        "Authorization":f"Bearer {token}"  
    }
    endpoint="http://localhost:8000/api/products/"
    get_response=requests.get(endpoint,headers=header)
    print(get_response.json())