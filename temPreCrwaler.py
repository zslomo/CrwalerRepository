# -*- coding: utf-8 -*-
import re
import requests
import urllib
#爬取预测数据
file = 'data/spotMarket/spot2017.csv'
wfile = 'data/spotMarket/sportAnalysis.csv'

data = requests.get('http://www.jepx.org/market/excel/spot_2017.csv').content
with open(file,'wb') as code:
     code.write(data)
