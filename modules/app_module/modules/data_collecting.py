import datetime
import os.path

from ADT.weather_ADT import *
from modules.secondary_functions import *

def main():
    save_path = "C:\\Users\schwajka\Desktop\CS@UCU\coding\COURSE PROJECT\core\modules\collected_data_from_lviv_to_odessa\\"
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    hours = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
    routes = [['lviv', 'odesa']]

    point_A = input("Enter the address of the start of your journey: ")
    point_B = input("Enter the address of the end of your journey: ")
    point_A = '+'.join(point_A.split())
    point_B = '+'.join(point_B.split())
    month = int(input("Enter the departure month: "))
    day = int(input("Enter the departure day: "))
    hour = int(input("Enter the departure hour: "))
    minute = int(input("Enter the departure minute: "))
    month, day, hour, minute = 5, 19, 20, 0
    departure_time = datetime.datetime(2017, month, day, hour, minute).timestamp()
    coors_list, filenames, temp = [], [], []
    route_data = get_data_from_URL(create_destination_url(point_A, point_B, int(departure_time)))

    # gets the route from the maps API
    for step in route_data['routes'][0]['legs'][0]['steps']: # creates a list of tuples each containing the end and the
        #  start location of the given route segment that can be included in an API url
        coors_list.append(((str(step['start_location']['lat']) + ',' + str(step['start_location']['lng'])),
                           (str(step['end_location']['lat']) + ',' + str(step['end_location']['lng']))))

    for route in routes:
        for month in months:
            for hour in hours:

                day, minute = 15, 0
                # month = m
                # hour = h
                point_A, point_B = route
                departure_time = datetime.datetime(2017, month, day, hour, minute).timestamp()
                coors_list, filenames, temp = [], [], []
                route_data = get_data_from_URL(create_destination_url(point_A, point_B, int(departure_time)))

                # gets the route from the maps API
                for step in route_data['routes'][0]['legs'][0]['steps']:  # creates a list of tuples each containing the end
                    #  and the start location of the given route segment that can be included in an API url
                    coors_list.append(((str(step['start_location']['lat']) + ',' + str(step['start_location']['lng'])),
                                       (str(step['end_location']['lat']) + ',' + str(step['end_location']['lng']))))
                for i in range(len(coors_list)):
                    if os.path.isfile(save_path+'{}_{}_data{}.txt'.format(month, hour, i+1)):
                        break
                    if i != 0:
                        departure_time = int(departure_time)
                        departure_time += route_data['routes'][0]['legs'][0]['steps'][i]['duration']['value']
                        departure_time = str(departure_time)
                        weather = WeatherAPI(coors_list[i][0], departure_time, 1, 1, 0, 0, 1 ,1)
                    else:
                        weather = WeatherAPI(coors_list[i][0], departure_time, 1, 1, 0, 0, 1, 1)
                    weather_data = weather.weather_url()
                    pprint(weather_data['currently'])
                    with open(save_path+'{}_{}_data{}.txt'.format(month, hour, i+1), 'w') as outfile:
                        # outfile.write(routes[0][0])
                        # outfile.write(str(weather_data['currently']['apparentTemperature'])+'\n')
                        # outfile.write(str(datetime.datetime.fromtimestamp(int(weather_data['currently']['time'])))+'\n')
                        if 'summary' in weather_data['currently']:
                            outfile.write(str(weather_data['currently']['summary'])+'\n')
