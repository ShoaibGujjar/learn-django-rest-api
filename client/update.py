import requests

endpoint="http://localhost:8000/api/products/1/update/"
data={
    "title":"hello world my ols frind",
    "Price":129.90
}

get_response=requests.put(endpoint,json=data)
print(get_response.json())