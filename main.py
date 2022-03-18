import requests

url = "https://vrmapi.victronenergy.com/v2/users/193725/accesstokens/list"

payload={}
headers = {
  'X-Authorization': 'Token example'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)