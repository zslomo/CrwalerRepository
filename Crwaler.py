# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

baseUrl = 'http://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?'
baseUrl43 = 'http://www.data.jma.go.jp/obd/stats/etrn/view/hourly_a1.php?'

class DataCrwaler:
    def __init__(self, prec_no, block_no, day, file):
        if(prec_no == 43):
            self.url =baseUrl43
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

    def getTemperatureData(self):
        html = self.getHtml()
        if not html:
            return 'html is not exit'
        if(self.precNo == 43):
            k =2
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
                    #print(str(self.day) + ' ' + e[0] + ":00" + ',' + e[2] + '\n')
                    self.file.write(str(self.day) + ' ' + '0' + e[0] + ":00" + ',' + e[k] + '\n')
                else:
                    #print(str(self.day) + ' ' + e[0] + ":00" + ',' + e[4] + '\n')
                    self.file.write(str(self.day) + ' ' + e[0] + ":00" + ',' + e[k] + '\n')
            else:
                self.file.write(str(self.day) + ' ' + e[0] + ":00" + ',' + '\n')
        return 'success'
