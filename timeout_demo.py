import requests

resp=requests.get("https://httpbin.org/delay/5",timeout=7 )
print(resp.status_code)
