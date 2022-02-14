import csv
import pandas as pd
import seaborn as sns

rows = []

with open("starData.csv","r") as f :
  csvreader = csv.reader(f)
  for row in csvreader :
    rows.append(row)

header = rows[0]
starData = rows[1:]

header[0] = "Index"

distance = []

for data in starData :
    if float(data[2]) <= 100 :
        distance.append(data)

print(len(distance))

gravity = []
for data in starData :
    if float(data[5]) < 150 or float(data[5]) > 350:
        gravity.append(data)

print(len(gravity))

final_list = []
for data in distance :
    if data in gravity:
        final_list.append(data)


with open("filteredStars.csv","a+") as f :
    csvW = csv.writer(f)
    csvW.writerow(header)
    csvW.writerows(final_list)