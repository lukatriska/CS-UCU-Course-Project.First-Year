import urllib.request
import urllib.parse
import json

request_url = "https://api.darksky.net/forecast/44975392fb2412c8cafe53735e7e720a/49.8396,24.0297?units=si&exclude=hourly,daily,flags"

def get_data_from_URL():
    with urllib.request.urlopen(request_url) as response: # read the response from the response object
        data = json.load(response) # reads the data from a json file

    return data

data = get_data_from_URL()


print(json.dumps(data, indent=2)) # prints the data line by line