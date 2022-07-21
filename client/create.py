import requests

endpoint="http://localhost:8000/api/products/"

data={
    "title":"this fiel is done",
    "Price":100
}

get_response=requests.post(endpoint,json=data)
print(get_response.json())