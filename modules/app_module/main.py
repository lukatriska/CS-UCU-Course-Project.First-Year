from modules import data_collecting, data_processing
from ADT import weather_ADT_test

file = input("Which file fo you want to run? data_collecting - dc; data_processing - dp; WeatherADT_test - wat: ")

if file == 'dc':
    data_collecting.main()
elif file == 'dp':
    data_processing.main()
elif file == 'wat':
    weather_ADT_test.main()
