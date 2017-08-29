# -*- coding: utf-8 -*-


#启动爬虫

import Crwaler as cr
import datetime
import sqlite3

# 东京都，千叶，神奈川，琦玉，山梨，茨城，群马
prec_nos = ['44','45','46', '43', '49', '40', '42']
precMap = {'44': 'Tokyo', '45': 'Chiba', '46': 'Yokokama', '43': 'Saitama', '49': 'Kafu', '40': 'Mito',
           '42': 'Maebashi'}
# 东京，千叶，横滨，琦玉，甲府，水户，前桥
block_nos = ['47662', '47682', '47670', '0363', '47638', '47629', '47624']
blockMap = {'47662': '东京', '47682': '千叶', '47670': '横滨', '0363': '琦玉', '47638': '甲府', '47629': '水户', '47624': '前桥'}
prec_block = {'44': '47662', '45': '47682', '46': '47670', '43': '0363', '49': '47638', '40': '47629', '42': '47624'}


class lancher:
    def runCrwaler(self):
        #dataFileBase = 'data/temperature/'
        for p in prec_nos:
            self.dateController(p)

    def dateController(self, p):
        conn = sqlite3.connect('temprature.db')
        c = conn.cursor()
       # fileLoc = fb + p + '.csv'
        #f = open(fileLoc, 'w+')
        begin = datetime.datetime.strptime(c.execute('''SELECT * FROM tableDate WHERE tablename ='''+precMap[p]),'%d/%m%Y')
        print(begin)
        end = datetime.date.today()
        for i in range((end - begin).days + 1):
            day = begin + datetime.timedelta(days=i)
            print(day)
            #cr.DataCrwaler(p, prec_block[p], day, f).getTemperatureData()
        #f.close()

run = lancher()
run.runCrwaler()
