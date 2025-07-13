import requests
from pprint import pprint

API_URL = 'http://localhost:8000/test'

response = requests.get(API_URL)
print(response)
print(response.status_code)
pprint(response.json())