from pprint import pprint

base = 'C:\\Users\schwajka\Desktop\CS@UCU\coding\COURSE PROJECT\core'

segments, months_data = [], []
data, summ_dict = {}, {}
months = [1, 2, 3, 4, 5, 6, 7] # only 7 months because that's all the data I could collect (only 1000 requests\day)
hours = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

# Reads the .txt files and puts all the info in them into a data dictionary with dictionaries
for month in months:
    data[month] = {}
    for hour in hours:
        data[month][hour] = {}
        for segment in range(1, 21):
            data[month][hour][segment] = {}
            with open(base+'\modules\collected_data_from_lviv_to_kyiv_jan-apr\{}_{}_data{}.txt'.format(month, hour, segment), 'r') as file:
                data[month][hour][segment] = file.readlines()[-1][:-1]

# Loops through the data dictionary and creates the counters of how may times a certain weather summary appears in the
# data dictionary
for month in months:
    summ_dict[month] = {}
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
                    summ_dict[month][hour]['Foggy'] += 1

# Loops through the sum_dict dictionary, leaving only the most frequent summary of a certain hour
for month in months:
    for hour in hours:
        temp = []
        for key, value in summ_dict[month][hour].items():
            temp.append(value)
        maxi = max(temp)
        maxi = [k for k, v in summ_dict[month][hour].items() if v == maxi]
        summ_dict[month][hour] = maxi[0]

pprint(summ_dict)
