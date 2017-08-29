# -*- coding: utf-8 -*-

# 爬虫部分
import re
import requests
import sqlite3

baseUrl = 'http://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?'
baseUrl43 = 'http://www.data.jma.go.jp/obd/stats/etrn/view/hourly_a1.php?'
precMap = {'44': 'Tokyo', '45': 'Chiba', '46': 'Yokokama', '43': 'Saitama', '49': 'Kafu', '40': 'Mito',
           '42': 'Maebashi'}


class DataCrwaler:
    def __init__(self, prec_no, block_no, day, file):
        if (prec_no == 43):
            self.url = baseUrl43
        else:
            self.url = baseUrl
        self.precNo = prec_no
        self.blockNo = block_no
        self.day = day
        self.file = file

    def getHtml(self):
        urlCrr = self.url + 'prec_no=' + \
                 str(self.precNo) + '&' + 'block_no=' + \
                 str(self.blockNo) + '&' + 'year=' + \
                 str(self.day.year) + '&' + 'month=' + \
                 str(self.day.month) + '&' + 'day=' + \
                 str(self.day.day) + '&view='

        html = requests.get(urlCrr).text
        print(urlCrr)
        return html

    # 不同的网页规则用不同的匹配方法
    def insertToDatabase(self, c, day, hour, temp):
        data = '\'' + day + '\'' + ',' + '\'' + hour + '\'' + ',' + temp
        sql = ''' INSERT INTO ''' + precMap[self.precNo] + '''VALUES ({})'''.format(data)
        print(sql)
        c.execute(sql)

    def getTemperatureData(self):
        conn = sqlite3.connect('temprature.db')
        c = conn.cursor()

        html = self.getHtml()
        if not html:
            return 'html is not exit'
        if (self.precNo == 43):
            k = 2
            reg = r'<tr class="mtx" style="text-align:right;"><td style="white-space:nowrap">(.*?)</td>' \
                  r'<td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td>' \
                  r'<td class="data_0_0">(.*?)</td><td class="data_0_0" style="text-align:center">(.*?)</td>' \
                  r'<td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td></tr>'
        else:
            k = 4
            reg = r'<tr class="mtx" style="text-align:right;"><td style="white-space:nowrap">(.*?)</td>' \
                  r'<td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td>' \
                  r'<td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td>' \
                  r'<td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td>' \
                  r'<td class="data_0_0" style="text-align:center">(.*?)</td>' \
                  r'<td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td>' \
                  r'<td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td><td class="data_0_0">(.*?)</td>' \
                  r'<td class="data_0_0">(.*?)</td></tr>'
        tempDataReg = re.compile(reg)
        tempDatalist = re.findall(tempDataReg, html)
        for e in tempDatalist:
            if e[k] != '' and e[k] != 'Ã':
                if (int(e[0]) < 10):
                    self.insertToDatabase(c, str(self.day), e[0], e[k])
                else:
                    self.insertToDatabase(c, str(self.day), e[0], e[k])
            else:
                self.insertToDatabase(c, str(self.day), e[0], e[k])
        conn.commit()
        conn.close()
        return 'success'
