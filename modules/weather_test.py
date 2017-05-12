from weather_ADT import *
from secondary_functions import *
import datetime


point_A = input("Enter the address of the start of your journey: ")
point_B = input("Enter the address of the end of your journey: ")
point_A = '+'.join(point_A.split())
point_B = '+'.join(point_B.split())
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
    coors_list.append(((str(step['start_location']['lat']) + ',' + str(step['start_location']['lng'])),
                       (str(step['end_location']['lat']) + ',' + str(step['end_location']['lng']))))

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


for i in range(len(final_data)):
    print("\n\t\tSEGMENT {}\n".format(i+1))
    for j in range(len(final_data[i])):
        if j == 0:
            print("Temperature: \t", final_data[i][j])
        elif j == 1:
            print("Time: \t\t\t", final_data[i][j])
        elif j == 2:
            print("From: \t\t\t", final_data[i][j])
        elif j == 3:
            print("To: \t\t\t", final_data[i][j])
        elif j == 4:
            print("Distance: \t\t", final_data[i][j])
        elif j == 5:
            print("Duration: \t\t", final_data[i][j])
        elif j == 6:
            print("Weather summary:", final_data[i][j])

