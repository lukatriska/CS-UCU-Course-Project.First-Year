# This program takes input of the start point, end point and time and shows the weather conditions for the route that it
# creates.

import json
import urllib.parse
import urllib.request
import datetime

maps_request_url_base = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyB2p2SUnKETTTjg0Lwo0IdS072Yfzckxds"
destination_url_base = "https://maps.googleapis.com/maps/api/directions/json?key=AIzaSyBp1OR4hAATTla6MPfQRdsR4Srn9rs4CFg"
# dark_request_url_example = "https://api.darksky.net/forecast/44975392fb2412c8cafe53735e7e720a/49.8396,24.0297?units=si&exclude=daily,flags"
# maps_request_url_example = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyB2p2SUnKETTTjg0Lwo0IdS072Yfzckxds&address=New+York"
# destination_url_example = "https://maps.googleapis.com/maps/api/directions/json?key=AIzaSyBp1OR4hAATTla6MPfQRdsR4Srn9rs4CFg&origin=Lviv+Ukraine&destination=Kiev+Ukraine&arrival_time=1494839532"

def create_destination_url(a, b, depart_time):
    """
    Adds the remaining information to the destination_url_base, including the starting and ending points and time.
    :param a: point a
    :type a: str
    :param b: point b
    :type b: str
    :param depart_time: departure time 
    :type depart_time: str
    :return: the final destination url
    :rtype: str
    """
    destination_url = destination_url_base + "&origin=" + a + "&destination=" + b + "&arrival_time=" + str(int(depart_time))
    return destination_url

def get_data_from_URL(url):
    """
    Gets data from a given URL in a JSON format.
    :param url: url
    :type url: str
    :return: data from the url
    :rtype: dict / list
    """
    with urllib.request.urlopen(url) as response: # read the response from the response object
        data = json.load(response) # reads the data from a json file
    return data

def address_to_coors(address):
    """
    Converts the address from normal view (e. g. "Lviv, Ukraine") to geographical coordinates (e. g. 49.8396,24.0297)
    :param address: desired address
    :type address: str
    :return: geographical coordinates of that address
    :rtype: str
    """
    address = address.replace(' ', '+')
    maps_request_url = maps_request_url_base + "&address=" + address
    maps_data = get_data_from_URL(maps_request_url)
    lat = maps_data['results'][0]['geometry']['location']['lat']
    lng = maps_data['results'][0]['geometry']['location']['lng']
    coors = '{0},{1}'.format(str(lat), str(lng))
    return coors

def coors_to_address(coors):
    """
    Converts the given geographical coordinates to a readable address.
    :param coors: geographical coordinates
    :type coors: str
    :return: readable address
    :rtype: str
    """
    maps_request_url = maps_request_url_base + "&address=" + coors
    maps_data = get_data_from_URL(maps_request_url)
    return maps_data['results'][0]['formatted_address']


class WeatherAPI:
    """
    An object of this class represents a weather forecast for a particular place and in a particular time  
    """
    DARKSKY_BASE_URL = "https://api.darksky.net/forecast/44975392fb2412c8cafe53735e7e720a/"
    GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyB2p2SUnKETTTjg0Lwo0IdS072Yfzckxds&"

    def __init__(self, address, time, currently=1, minutely=1, hourly=1, daily=1, alerts=1, flags=1):
        self.exclude_lst = []
        self.address = address
        self.time = time
        self.dark_sky_url = self.DARKSKY_BASE_URL + address_to_coors(address) + ',' + str(int(self.time)) + '?units=si&'
        if currently or minutely or hourly or daily or alerts or flags == 0: # adds items to exclude
            self.dark_sky_url += 'exclude='
            if currently == 0:
                self.exclude_lst.append('currently')
            if minutely == 0:
                self.exclude_lst.append('minutely')
            if hourly == 0:
                self.exclude_lst.append('hourly')
            if daily == 0:
                self.exclude_lst.append('daily')
            if alerts == 0:
                self.exclude_lst.append('alerts')
            if flags == 0:
                self.exclude_lst.append('flags')
            for i in range(len(self.exclude_lst)):
                if i > 0:
                    self.dark_sky_url += ','
                self.dark_sky_url += self.exclude_lst[i]

    def address(self):
        """
        Returns address of the request
        :return: address (str)
        """
        return self.address

    def time(self):
        """
        Returns the time of request
        :return: time 
        """
        return self.time

    def weather_url(self):
        """
        Returns the final Dark Sky API JSON file, considering the address, the time and the list of items to exclude (if
        such exist)
        :return: json file 
        """
        return get_data_from_URL(self.dark_sky_url)





def final():

    # point_A = input("Enter the address of the start of your journey: ")
    # point_B = input("Enter the address of the end of your journey: ")
    # point_A = '+'.join(point_A.split())
    # point_B = '+'.join(point_B.split())
    point_A = 'lviv+ukraine'
    point_B = 'kyiv+ukraine'
    month = int(input("Enter the departure month: "))
    day = int(input("Enter the departure day: "))
    hour = int(input("Enter the departure hour: "))
    minute = int(input("Enter the departure minute: "))
    print("\nplease wait...\n\nthis takes about a minute, depending on your Internet connection\n\nin the meantime, here's a "
          "joke: \nInterviewer: What's your biggest strength?\nMe: I'm a fast learner.\nInterviewer: What's 11 * 11?\nMe:"
          " 65.\nInterviewer: Not even close. It's 121.\nMe: It's 121.\n")
    departure_time = datetime.datetime(2017, month, day, hour, minute).timestamp()
    coors_list, final_data = [], []
    route_data = get_data_from_URL(create_destination_url(point_A, point_B, int(departure_time))) # gets the route from the maps API
    for step in route_data['routes'][0]['legs'][0]['steps']: # creates a list of tuples each containing the end and the
        #  start location of the given route segment that can be included in an API url
        coors_list.append(((str(step['end_location']['lat']) + ',' + str(step['start_location']['lng'])),
                           (str(step['start_location']['lat']) + ',' + str(step['start_location']['lng']))))

    for i in range(len(coors_list)):
        if i != 0:
            departure_time = int(departure_time)
            departure_time += route_data['routes'][0]['legs'][0]['steps'][i]['duration']['value']
            departure_time = str(departure_time)
            weather = WeatherAPI(coors_list[i][0], departure_time, 1, 1, 0, 0, 1 ,0)
        else:
            weather = WeatherAPI(coors_list[i][0], departure_time, 1, 1, 0, 0, 1, 0)
        weather_data = weather.weather_url()
        temp = []
        temp.append(weather_data['currently']['apparentTemperature'])
        temp.append(datetime.datetime.fromtimestamp(int(weather_data['currently']['time'])))
        temp.append(coors_to_address(coors_list[i][0]))
        temp.append(coors_to_address(coors_list[i][1]))
        temp.append(route_data['routes'][0]['legs'][0]['steps'][i]['distance']['text'])
        temp.append(route_data['routes'][0]['legs'][0]['steps'][i]['duration']['text'])
        temp.append(weather_data['currently']['summary'])
        final_data.append(temp)
    return final_data

# final()

to_print = final()

# x = [[14.38, datetime.datetime(2017, 5, 18, 11, 11), "Krakivska Street, 34, L'viv, Lviv Oblast, Ukraine", "Miskevycha Square, 9, L'viv, Lviv Oblast, Ukraine", '0.6 km', '3 mins', 'Clear', '\n'], [14.38, datetime.datetime(2017, 5, 18, 11, 11, 12), "Rizni Square, 1, L'viv, Lviv Oblast, Ukraine", "Svobody Ave, 26, L'viv, Lviv Oblast, Ukraine", '43 m', '1 min', 'Clear', '\n'], [14.48, datetime.datetime(2017, 5, 18, 11, 15, 9), "Remisnycha Street, 8, L'viv, Lviv Oblast, Ukraine", "Rizni Square, 1А, L'viv, Lviv Oblast, Ukraine", '1.4 km', '4 mins', 'Clear', '\n'], [14.6, datetime.datetime(2017, 5, 18, 11, 20, 5), "Sheremety St, 26-30, L'viv, Lviv Oblast, Ukraine", "Viacheslava Chornovola Ave, 59, L'viv, Lviv Oblast, Ukraine", '2.6 km', '5 mins', 'Clear', '\n'], [14.89, datetime.datetime(2017, 5, 18, 11, 32, 3), 'Е372, Lviv Oblast, Ukraine', "Lypynskoho St, 58, L'viv, Lviv Oblast, Ukraine", '10.9 km', '12 mins', 'Clear', '\n'], [18.26, datetime.datetime(2017, 5, 18, 13, 44, 46), 'Р15, Lviv Oblast, Ukraine', 'М06, Mali Pidlisky, Lviv Oblast, Ukraine', '186 km', '2 hours 13 mins', 'Clear', '\n'], [17.43, datetime.datetime(2017, 5, 18, 13, 57, 49), "вулиця Рольщикова, Velyka Omelyana, Rivnens'ka oblast, Ukraine, 35360", "М06, Rivnens'ka oblast, Ukraine", '17.0 km', '13 mins', 'Clear', '\n'], [18.94, datetime.datetime(2017, 5, 18, 13, 58, 17), "Р05, Rivnens'ka oblast, Ukraine", "Kyivs'ka St, Rivnens'ka oblast, Ukraine", '0.5 km', '1 min', 'Clear', '\n'], [19.28, datetime.datetime(2017, 5, 18, 15, 23, 25), "Unnamed Road, Ukrainka, Rivnens'ka oblast, Ukraine", "М06, Rivnens'ka oblast, Ukraine", '136 km', '1 hour 25 mins', 'Clear', '\n'], [19.15, datetime.datetime(2017, 5, 18, 17, 14, 24), "М06, Kurne, Zhytomyrs'ka oblast, Ukraine, 12030", "М06, Zhytomyrs'ka oblast, Ukraine", '172 km', '1 hour 51 mins', 'Clear', '\n'], [17.72, datetime.datetime(2017, 5, 18, 17, 24, 48), 'Kiltseva Rd, 30, Kyiv, Ukraine', 'Peremohy Ave, 115А, Kyiv, Ukraine', '9.6 km', '10 mins', 'Clear', '\n'], [17.71, datetime.datetime(2017, 5, 18, 17, 25, 38), 'Zhylianska St, 160, Kyiv, Ukraine', 'Peremohy Ave, 1, Kyiv, Ukraine', '0.2 km', '1 min', 'Clear', '\n'], [17.7, datetime.datetime(2017, 5, 18, 17, 26, 26), 'Dmytrivska St, 2, Kyiv, Ukraine', 'Peremohy Square, 1, Kyiv, Ukraine', '0.1 km', '1 min', 'Clear', '\n'], [17.64, datetime.datetime(2017, 5, 18, 17, 30, 6), 'Hoholivska St, 29, Kyiv, Ukraine', 'Olesia Honchara St, 79, Kyiv, Ukraine', '1.2 km', '4 mins', 'Clear', '\n'], [17.63, datetime.datetime(2017, 5, 18, 17, 30, 42), 'Olesia Honchara St, 17А, Kyiv, Ukraine', 'Olesia Honchara St, 20, Kyiv, Ukraine, 01-001', '0.1 km', '1 min', 'Clear', '\n'], [17.59, datetime.datetime(2017, 5, 18, 17, 33, 5), 'Velyka Zhytomyrska St, 32, Kyiv, Ukraine', "Strilets'ka St, 15, Kyiv, Ukraine", '0.6 km', '2 mins', 'Clear', '\n'], [17.56, datetime.datetime(2017, 5, 18, 17, 34, 54), "Strilets'ka St, 4, Kyiv, Ukraine", 'Velyka Zhytomyrska St, 16, Kyiv, Ukraine', '0.5 km', '2 mins', 'Clear', '\n'], [17.54, datetime.datetime(2017, 5, 18, 17, 36, 23), 'Tarasa Shevchenka Ln, 8А, Kyiv, Ukraine, 02000', 'Velyka Zhytomyrska St, 2А, Kyiv, Ukraine', '0.5 km', '1 min', 'Clear', '\n'], [17.53, datetime.datetime(2017, 5, 18, 17, 36, 49), 'Khreschatyk St, 20-22, Kyiv, Ukraine', 'Pamyatnik fonaryam i stulyam., Maidan Nezalezhnosti, Kyiv, Ukraine, 02000', '0.1 km', '1 min', 'Clear', '\n'], [17.53, datetime.datetime(2017, 5, 18, 17, 36, 57), 'Khreschatyk St, 20, Kyiv, Ukraine', 'ulitsa Institutskaya, 2, Kyiv, Ukraine', '71 m', '1 min', 'Clear', '\n']]

for i in to_print:
    for j in i:
        print(j)
    print("\n")

# print('icon: \t\t\t\t', weather_data['currently']['icon'])
# print('precipIntensity: \t', weather_data['currently']['precipIntensity'])
# print('precipProbability: \t', weather_data['currently']['precipProbability'])
# weather_data = weather.weather_url()
# weather = WeatherAPI("Lviv Ukraine", departure_time, 1, 1, 0, 0, 1, 0)
# print('apparentTemperature:', weather_data['currently']['apparentTemperature'])
# print('icon: \t\t\t\t', weather_data['currently']['icon'])
# print('precipIntensity: \t', weather_data['currently']['precipIntensity'])
# print('precipProbability: \t', weather_data['currently']['precipProbability'])
# print('summary: \t\t\t', weather_data['currently']['summary'])
# print(datetime.datetime.fromtimestamp(int(weather_data['currently']['time'])))
# print(weather_data['latitude'], weather_data['longitude'])
# pprint()

# print("\n\n\t\t THE DESTINATION MAPS RESPONSE\n")
