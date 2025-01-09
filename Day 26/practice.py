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
import math

data = pandas.read_csv("Day 26\weather_data.csv")
#print(data)
#print(data["temp"])
lis = pandas.Series(data["temp"])

#print(lis)

ave = lis.mean()
print(f"The average is : {ave}")
max_val = lis.max()
print(f"The max value of temp is : {max_val}")
print(data[data.temp == data.temp.max()])

mon = data[data.day == "Monday"]
print(mon)

temp_mon = int(mon["temp"])
print(int(temp_mon))

temp_in_f = (temp_mon * 1.8) + 32
print(f"The temperature in Faranheit is {temp_in_f}")

#creating dataframe from scratch

data_dict = {
    "students" : ["ab", "bc", "ca"],
    "marks" : [23, 50, 44] 
}
dat = pandas.DataFrame(data_dict)

print(dat)
