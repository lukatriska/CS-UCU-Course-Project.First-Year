import forecastio

api_key = "44975392fb2412c8cafe53735e7e720a"
lat = 49.8396830
lng = 24.0297170

forecast = forecastio.load_forecast(api_key, lat, lng)

byHour = forecast.hourly()

print(byHour.summary)
print(byHour.icon)

for hourlyData in byHour.data:
    print(hourlyData.temperature)
    print(hourlyData.summary)


import urllib.request
import urllib.parse
import json
BASE_URL = "https://api.darksky.net/forecast/44975392fb2412c8cafe53735e7e720a/49.8396,24.0297"
params = { 'locations': "48.5000,23.2703"}
def get_data_from_URL():
    # params_str = urllib.parse.urlencode(params)
    request_url = "https://api.darksky.net/forecast/44975392fb2412c8cafe53735e7e720a/49.8396,24.0297"
    request = urllib.request.Request(request_url)
    with urllib.request.urlopen(request_url) as response: # read the response from the response object
        data = response.read() # decode it from bytes to string
        data = data.decode("utf-8") # parse the string into a python object of dictionaries and lists
        json.loads(data)
    return data

data = get_data_from_URL()

# for i in data:
#     print(i)
print(data)

# import urllib
#
# link = "https://api.darksky.net/forecast/0123456789abcdef9876543210fedcba/42.3601,-71.0589"
# f = urllib.urlopen(link)
# myfile = f.read()
# print(myfile)


# import requests
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)
# r.json()

# import urllib, json
# # import urllib.request
#
# url = "https://api.darksky.net/forecast/0123456789abcdef9876543210fedcba/42.3601,-71.0589"
# response = urllib.request.urlopen(url)
# data = json.loads(response.read())
# print(data)

# import urllib.request
# req = urllib.request.Request('https://api.darksky.net/forecast/44975392fb2412c8cafe53735e7e720a/42.3601,-71.0589',
#                              headers={'User-Agent': 'Mozilla/5.0'})
# ttest = urllib.request.urlopen(req).read()
#
# print("AWdawdd ")
#
# print(ttest)