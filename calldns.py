import requests
req= requests.get('https://w3schools.com')
print(req.status_code)
if req.status_code == 200:
   print(True, req.status_code)

