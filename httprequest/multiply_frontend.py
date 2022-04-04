'''
This code for sending GET request to the backend API, and then get the results that will be displayed on the console.
'''

import requests
payload = {"param1": 4,"param2":6}

def getmultiply(payload):
  result = requests.get("http://backend:8000/multiply", params=payload)
  return (result.json())

print(getmultiply(payload))
