import csv
import pandas

with open("weather_data.csv") as csv_data:
    data = csv.reader(csv_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

data = pandas.read_csv("weather_data.csv")
print(data["temp"])