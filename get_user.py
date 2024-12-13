import requests

p={"page":2}

resp=requests.get("https://reqres.in/api/users",params=p)
print(resp.url)
json_resp=resp.json()

print(json_resp['total'])
assert json_resp['total']==12
print(json_resp['total_pages'])
assert json_resp['total_pages']==2, "Total pages count is not matching"
print(json_resp["data"][0]["email"])
assert (json_resp["data"][0]["email"]).endswith("reqres.in"),"email format is not matching"
print (json_resp["data"][0]["first_name"])
assert (json_resp["data"][0]["first_name"])!=None
print(json_resp["data"][2]["last_name"])
assert (json_resp["data"][2]["last_name"]).startswith("Funke"),"Not matching"
print(json_resp["support"]["url"])
assert json_resp["support"]["url"]!=None