import csv

dataFile = 'data/temperature/Data_by0823.csv'

totalFile = 'data/temperature/total.csv'

with open(dataFile, newline='') as csvfile1:
    reader = csv.reader(csvfile1)
    data = [[row[0], row[40], row[112], row[76], row[7], row[256], row[220], row[148]] for row in reader]

with open(totalFile, newline='') as csvfile:
    reader = csv.reader(csvfile)
    crwalerData = [[row[0], row[1], row[2], row[3], row[4], row[5], row[6]] for row in reader]
diff = 0
for i in range(75623):
    for j in range(6):
        if (data[i][j + 1] != crwalerData[i][j]):
            diff += 1
            print(str(data[i][0]) + '---' + str(j) + '---' + str(data[i][j + 1]) + '---' + str(crwalerData[i][j]))
print(diff)
