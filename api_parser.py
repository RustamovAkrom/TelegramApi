import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5ODUzMzQxLCJpYXQiOjE3MTk3NjY5NDEsImp0aSI6Ijg5MDk3ZGNhYjU5NDQ1NThhNzIwMjU1ZTgyZDhmYjg5IiwidXNlcl9pZCI6MX0.RefXRF0Y3zUdRl-q3DYTLHt1M7D4IOA95pM6T0Tyzr0"
BASE_URL = "http://127.0.0.1:8000/en/api/v1/"


headers = {
    "Authorization": f"Bearer {TOKEN}"
}
response = requests.get(BASE_URL + "account/saved-message-retrive/1", headers=headers)

print(response.json())