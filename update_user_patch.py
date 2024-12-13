import json
import requests
payload={
    "name": "API",

}

#print(type(data))
resp=requests.patch("https://reqres.in/api/users/2",data=payload)
print(resp)
print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()["name"]=="API"