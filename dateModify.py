import datetime

prec_nos = ['44', '45', '46', '43', '49', '40', '42']
precMap = {'44': '东京都', '45': '千叶', '46': '神奈川', '43': '琦玉', '49': '山梨', '40': '茨城', '42': '群马'}

fileBase = 'C:\\Users\\i344856\\Desktop\\TemperatureData\\'
for e in prec_nos:
    file = fileBase + e + '.csv'
    wfile = fileBase + precMap[e] + '.csv'
    f = open(file, 'r')
    wf = open(wfile, 'w+')
    while 1:
        line = f.readline()
        if not line:
            break
        datetimeStr = line.split(',')[0]
        temp = line.split(',')[1]
        if datetimeStr.split(' ')[1] == '24:00':
            time = datetime.datetime.strptime(datetimeStr.replace(' 24:00', ' 23:00'), '%Y-%m-%d %H:%M')
            time += datetime.timedelta(hours=1)
            w = str(time).replace('00:00:00', '00:00') + ',' + temp
            print(w)
            wf.write(w)
        else:
            print(line)
            wf.write(line)
    f.close()
    wf.close()
