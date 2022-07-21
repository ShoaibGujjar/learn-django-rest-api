import requests

endpoint="http://localhost:8000/api/products/11111111111111111/"


get_response=requests.get(endpoint)
print(get_response.json())