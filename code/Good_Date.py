# -*- coding: utf-8 -*-

import pandas as pd

inputfile = '../date/1.csv'  # 评论汇总文件

outputfile = '../date/good.txt'  # 评论提取后保存路径

data = pd.read_csv(inputfile, encoding='utf-8')

data = data[[u'评价内容']][data[u'评价星级'] == u'star5']

data.to_csv(outputfile, index=False, header=False, encoding='utf-8')
