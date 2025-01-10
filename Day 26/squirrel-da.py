import pandas

data = pandas.read_csv(r"Day 26\Squirrel_Census_Data.csv")

dh = data.head(5)
print(dh)

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(f"The number of Gray fur squirrels is {grey_squirrels}")
print(f"The number of Cinnamon fur squirrels is {cinnamon_squirrels}")
print(f"The number of Black fur squirrels is {black_squirrels}")

data_dict = {
    "Fur Color" : ["Gray" , "Cinnamon" , "Black"],
    "Count" : [grey_squirrels,cinnamon_squirrels,black_squirrels]
}

data_f = pandas.DataFrame(data_dict)

print(data_f)