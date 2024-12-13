import json
import requests
payload={
    "name": "API",
    "job": "API Testing"
}

#print(type(data))
resp=requests.put("https://reqres.in/api/users/2",data=payload)
print(resp)
print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()["job"]=="API Testing"
