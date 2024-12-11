#api
import requests
response = requests.get("https://www.randomuser.me/api/")
print(response)
response.text

#for install :   pip install requests
