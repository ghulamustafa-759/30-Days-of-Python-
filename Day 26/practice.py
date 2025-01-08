# with open("Day 26\weather_data.csv") as datafile:
#     data = datafile.readlines()
#     print(data)

# import csv

# with open("Day 26\weather_data.csv") as datafile:
#     data = csv.reader(datafile) #csv.reader turns the data into an object, can be iterated using a loop
#     print(data)
#     temperatures = []
#     for i in data:
#         if i[1] != 'temp':
#             temperatures.append(int(i[1]))
    
#     print (temperatures)

import pandas

data = pandas.read_csv("Day 26\weather_data.csv")
print(data)
print(data["temp"])