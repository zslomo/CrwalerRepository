# -*- coding: utf-8 -*-
import Crwaler as cr
import datetime
import psycopg2 as ps

# 东京都，千叶，神奈川，琦玉，山梨，茨城，群马
prec_nos = ['44','45','46', '43', '49', '40', '42']
precMap = {'44': '东京都', '45': '千叶', '46': '神奈川', '43': '琦玉', '49': '山梨', '40': '茨城', '42': '群马'}
# 东京，千叶，横滨，琦玉，甲府，水户，前桥
block_nos = ['47662', '47682', '47670', '0363', '47638', '47629', '47624']
blockMap = {'47662': '东京', '47682': '千叶', '47670': '横滨', '0363': '琦玉', '47638': '甲府', '47629': '水户', '47624': '前桥'}
prec_block = {'44': '47662', '45': '47682', '46': '47670', '43': '0363', '49': '47638', '40': '47629', '42': '47624'}


class lancher:
    def runCrwaler(self):
        dataFileBase = 'data/temperature/'
        for p in prec_nos:
            self.dateController(p, dataFileBase)

    def dateController(self, p, fb):
        fileLoc = fb + p + '.csv'
        f = open(fileLoc, 'w+')
        begin = datetime.date(2009, 1, 1)
        end = datetime.date(2017, 8, 17)
        for i in range((end - begin).days + 1):
            day = begin + datetime.timedelta(days=i)
            print(day)
            cr.DataCrwaler(p, prec_block[p], day, f).getTemperatureData()
        f.close()

run = lancher()
run.runCrwaler()
