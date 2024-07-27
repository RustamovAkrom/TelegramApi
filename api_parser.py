import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5OTk2NDQ0LCJpYXQiOjE3MTk5MTAwNDQsImp0aSI6ImRmMGYyZmFhYmFkYTRlZTY4Y2UwMmFiZmU4Njk3MTFkIiwidXNlcl9pZCI6MX0.aVQokdOUaQW3CsWIHYnWxt0S_96_v_pyukpYy6ZjKjA"
BASE_URL = "http://127.0.0.1:8000/en/api/v1/"


headers = {"Authorization": f"Bearer {TOKEN}"}
data = {"phone_number": "+998958786277", "token": TOKEN}

response = requests.get(BASE_URL + "account/user-activate/", data=data, headers=headers)

print(response.json())
print(response.status_code)
