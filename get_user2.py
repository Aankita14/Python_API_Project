import requests
resp=requests.get("https://reqres.in/api/users?page=2")
code=resp.status_code
assert code==200,"code doesn't match"
#print(resp.text)
#print(resp.content)
print(resp.json())
print(resp.headers)
print(resp.encoding)
print(resp.cookies)
print(resp.url)