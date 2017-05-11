#This file contains help functions for the Dark SKY Weather API

import json
import urllib.parse
import urllib.request

maps_request_url_base = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyB2p2SUnKETTTjg0Lwo0IdS072Yfzckxds"
destination_url_base = "https://maps.googleapis.com/maps/api/directions/json?key=AIzaSyBp1OR4hAATTla6MPfQRdsR4Srn9rs4CFg"


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
    print(maps_data)
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
