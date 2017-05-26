from statistics import mode
from pprint import pprint
import datetime

data = {}
routes = [['lviv', 'kiev'], ['lviv', 'odessa']]

for route in routes:
    with open('from_{}_to_{}_summary.txt'.format(route[0], route[1])) as file:
        data = eval(file.read())
    # pprint(data)
    most_pop = {}
    for month in data:
        temp = []
        ind_temp = []
        for hour, value in data[month].items():
            temp.append(value)
        most_pop[month] = [(mode(temp))]
        for i in range(len(temp)):
            if temp[i] == most_pop[month][0]:
                ind_temp.append(i)
        most_pop[month].append(ind_temp[int(len(ind_temp)/2)])

    safe_months = []
    for key, value in most_pop.items():
        if value[0] == 'Clear':
            safe_months.append([key, value[1]])
    print("The safest months to travel from {} to {}:".format(route[0], route[1]))
    for month, hour in safe_months:
        print("\t- {}, its safest hour of departure: {}".format(datetime.date(1900, month, 1).strftime('%B'), hour*2))
    print('\n')
