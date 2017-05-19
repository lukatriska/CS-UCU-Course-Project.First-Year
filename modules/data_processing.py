import json
from pprint import pprint
import operator

base = 'C:\\Users\schwajka\Desktop\CS@UCU\coding\COURSE PROJECT\core'

segments = []
months = [k + 1 for k in range(12)]
hours = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
hour = 2
month = 1

months_data = []
data = {}

# data[month] = []
# d

for month in months:
    data[month] = {}
    if month > 3:
        break
    for hour in hours:
        data[month][hour] = {}
        for segment in range(20):
            # print('{}_{}_data{}.txt'.format(month, hour, segment+1))
            data[month][hour][segment + 1] = {}
            with open(base+'\modules\collected_data_from_lviv_to_kyiv_jan-apr\{}_{}_data{}.txt'.format(month, hour, segment+1), 'r') as file:
                seg_data = file.readlines()
                # temper, date, summary = seg_data
                summary = seg_data[-1]
                # data[month][hour][segment+1]['temperature'] = temper
                # data[month][hour][segment+1]['date'] = date
                data[month][hour][segment+1] = summary[:-1]
pprint(data)

summ_dict =  {}

for month in months:
    summ_dict[month] = {}
    if month > 3:
        break
    for hour in hours:
        summ_dict[month][hour] = {}
        for segment in range(1, 21):
            if data[month][hour][segment] == 'Mostly Cloudy':
                if not 'Mostly Cloudy' in summ_dict[month][hour]:
                    summ_dict[month][hour]['Mostly Cloudy'] = 1
                else:
                    summ_dict[month][hour]['Mostly Cloudy'] += 1
            elif data[month][hour][segment] == 'Clear':
                if not 'Clear' in summ_dict[month][hour]:
                    summ_dict[month][hour]['Clear'] = 1
                else:
                    summ_dict[month][hour]['Clear'] += 1
            elif data[month][hour][segment] == 'Overcast':
                if not 'Overcast' in summ_dict[month][hour]:
                    summ_dict[month][hour]['Overcast'] = 1
                else:
                    summ_dict[month][hour]['Overcast'] += 1
            elif data[month][hour][segment] == 'Partly Cloudy':
                if not 'Partly Cloudy' in summ_dict[month][hour]:
                    summ_dict[month][hour]['Partly Cloudy'] = 1
                else:
                    summ_dict[month][hour]['Partly Cloudy'] += 1
            elif data[month][hour][segment] == 'Foggy':
                if not 'Foggy' in summ_dict[month][hour]:
                    summ_dict[month][hour]['Foggy'] = 1
                else:
                    # f = data[1][2]
                    summ_dict[month][hour]['Foggy'] += 1


pprint(summ_dict)

for month in months:
    if month > 3:
        break
    for hour in hours:
        summ_dict[month][hour] = sorted(summ_dict[month][hour].items(), key=operator.itemgetter(1)).reverse()

pprint(summ_dict)

















































































































































































# pprint(f)
                    # print(data[].keys())
                    # f = data[1][2]
                    # print(f.items())
                    # for i in f.items():
                    #     print(i[1]['summary'])

                    # most_clo, overcast, clear, part_clo, rainy, foggy = 0, 0, 0, 0, 0, 0
                    # for month in range(1, 4):
                    #     for hour in hours:
                    #         f = data[month][hour]
                    #         pprint(f.items())
                    #         for i in f.items():
                    #             if i[1]['summary'] == 'Mostly Cloudy\n':
                    #                 most_clo += 1
                    #                 # if not 'Mostly Cloudy' in summ_dict:
                    #                 #     summ_dict[month][hour]['Mostly Cloudy'] = 1
                    #                 # else:
                    #                 #     summ_dict[month][hour]['Mostly Cloudy'] += 1
                    #             elif i[1]['summary'] == 'Clear\n':
                    #                 clear += 1
                    #                 # if not 'Clear' in summ_dict[month][hour]:
                    #                 #     summ_dict[month][hour]['Clear'] = 1
                    #                 # else:
                    #                 #     summ_dict[month][hour]['Clear'] += 1
                    #             elif i[1]['summary'] == 'Overcast\n':
                    #                 overcast += 1
                    #             elif i[1]['summary'] == 'Partly Cloudy\n':
                    #                 part_clo += 1
                    #             elif i[1]['summary'] == 'Rainy\n':
                    #                 rainy += 1
                    #             elif i[1]['summary'] == 'Foggy\n':
                    #                 foggy += 1
                    #             # elif i[1]['summary'] == 'Overcast\n':
                    #             #     overcast += 1
                    #                 # if not 'Overcast' in summ_dict[month][hour]:
                    #                 #     summ_dict[month][hour]['Overcast'] = 1
                    #                 # else:
                    #                 #     summ_dict[month][hour]['Overcast'] += 1
                    #
                    # elif i[1]['summary'] == 'Mostly Cloudy\n':
                    # elif i[1]['summary'] == 'Mostly Cloudy\n':
                    # elif i[1]['summary'] == 'Mostly Cloudy\n':
                    # print(f.items())

                    # print(summ_dict)
                    # print('most_clo    \t', most_clo)
                    # print('partly cloudy   ', part_clo)
                    # print('clear   \t\t', clear)
                    # print('overcast    \t', overcast)
                    # print('rainy    \t\t', rainy)
                    # print('foggy    \t\t', foggy)

                    # if data[month][hour][segment] == 'Mostly Cloudy':
            #     if not 'Mostly Cloudy' in summ_dict[month][hour][segment]:
            #         summ_dict[month][hour][segment]['Mostly Cloudy'] = 1
            #     else:
            #         summ_dict[month][hour]['Mostly Cloudy'] += 1
