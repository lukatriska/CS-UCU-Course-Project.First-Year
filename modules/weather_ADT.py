# This program takes input of the start point, end point and time and shows the weather conditions for the route that it
# creates.

from secondary_functions import address_to_coors, get_data_from_URL


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
