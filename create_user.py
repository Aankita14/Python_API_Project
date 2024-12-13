import requests

payload={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

#print(type(data))
resp=requests.post("https://reqres.in/api/register",data=payload)
print(resp)
#print (type("resp"))
print(resp.json()["token"])
assert resp.json()["token"]=="QpwL5tke4Pnpja7X4"