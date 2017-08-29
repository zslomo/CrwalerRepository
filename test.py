import sqlite3
import csv

prec = ['Tokyo', 'Chiba', 'Yokokama', 'Saitama', 'Kafu', 'Mito', 'Maebashi']
conn = sqlite3.connect('temprature.db')

c = conn.cursor()
# with open('data/spotMarket/spotAnalysis.csv','r') as csvfile:
#     r = csv.reader(csvfile)
#     for row in r:
#         d = '\'' + row[0] + '\'' + ',' + '\'' + row[1] + '\'' + ',' + row[2]
#         print(d)
#         c.execute('INSERT INTO spotMarket VALUES ({})'.format(d))
# conn.commit()
# conn.close()



data = '\'' + 'spotMarket' + '\'' + ',' + '\'' + '8/26/2017' + '\'' + ',' + '\'' + '24' + '\''
i = ''' INSERT INTO tableDate VALUES ({})'''.format(data)
print(i)
c.execute(i)
conn.commit()
conn.close()




# conn = sqlite3.connect('temprature.db')
#
# c = conn.cursor()
# for e in prec:
#     file = 'data/temprature/' + e + '.csv'
#
#     with open(file, 'r') as csvfile:
#         r = csv.reader(csvfile)
#         lines = [line for line in r]
#     insert = 'INSERT INTO ' + e + ' VALUES '
#     c.execute('DELETE FROM ' + e)
#     for line in lines:
#
#         if not line[2] or line[2] == '///':
#             line[2] = 'null'
#         # print(line)
#         i = insert + '(' + '\'' + line[0] + '\'' + ',' + '\'' + line[1] + '\'' + ',' + line[2] + ',' + line[3] + ')'
#         print(i)
#         c.execute(i)
#     c.execute('SELECT * FROM ' + e)
#     print(c.fetchall())
# conn.commit()
# conn.close()













# f = 'data/spotMarket/spot2017.csv'
# wfile = 'data/spotMarket/spotAnalysis.csv'
# with open(f, 'rb') as csvfile:
#     lines = csvfile.readlines()
#     rows = [row for row in lines]
#
# wf = open(wfile,'w+')
# for i in range(1, len(rows), 2):
#     avg = (float(str(rows[i]).split(',')[4]) * float(str(rows[i]).split(',')[8]) \
#            + float(str(rows[i + 1]).split(',')[4]) * float(str(rows[i + 1]).split(',')[8])) / \
#           (float(str(rows[i]).split(',')[4]) + float(str(rows[i + 1]).split(',')[4]))
#     wf.write(str(rows[i]).split(',')[0].split('\'')[1]
#           + ',' + str(int(str(rows[i + 1]).split(',')[1]) / 2).split('.')[0]
#           + ',' +str(avg)+'\n')


# import pyhdb as ph
# import csv
#
# connection = ph.connect(
#     host="10.58.185.191",
#     port=30115,
#     user="TANBIN",
#     password="Abcd1234",
#     autocommit=True
# )
# cursor = connection.cursor()
#
#
# file = 'C:/Users/i344856/Desktop/TemperatureData/44.csv'
#
# with open(file, 'r') as csvfile:
#     r = csv.reader(csvfile)
#     lines = [line for line in r]
# insert = 'INSERT INTO TANBIN.TOKYO VALUES '
# cursor.execute('truncate table TANBIN.tokyo')
# for line in lines:
#     print(line)
#     cursor.execute(
#         insert + '(' + '\'' + line[0].split(' ')[0] + '\'' + ',' + '\'' + line[0].split(' ')[1]
#         + '\'' + ',' + line[1] + ',' + '0' + ')')
# cursor.close()
# connection.close()
