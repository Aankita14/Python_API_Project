import json

import requests

my_data=open("data.json","r").read()
payload={
    "name": "Ankita",
    "job": "QA"
}
#print(type(data))
resp=requests.post("https://reqres.in/api/users",data=json.loads(my_data))
print(resp)
print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()["job"]=="Python"