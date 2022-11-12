# Program to get data from weather API

# importing the  modules
import requests
import json

# input parameters for the API
parameters = {
    "lat": "60.19",
    "lon": "24.94",
    "product": "civil",
    "output": "json"
}

response = requests.get("http://www.7timer.info/bin/api.pl", params=parameters)
text = json.dumps(response.json(), sort_keys=True, indent=4)
print(text)

