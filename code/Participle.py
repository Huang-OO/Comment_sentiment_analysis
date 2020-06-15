# -*- coding: utf-8 -*-

import pandas as pd

import jieba  # 导入结巴分词，需要自行下载安装

# 参数初始化

inputfile1 = '../date/good_neg.txt'

inputfile2 = '../date/bad_pos.txt'

outputfile1 = '../date/good_neg_cut.txt'

outputfile2 = '../date/bad_pos_cut.txt'

data1 = pd.read_csv(inputfile1, encoding='utf-8', header=None)  # 读入数据

data2 = pd.read_csv(inputfile2, encoding='utf-8', header=None)

mycut = lambda s: ' '.join(jieba.cut(s))  # 自定义简单分词函数,先识别句子中的中文单词，然后把中文单词通过空格连接起来

# 上面一句代码中，s是入口参数，.join前面的空格表示把jieba库处理过后的s中的词语jieba.cut(s)，用空格来连接。

data1 = data1[0].apply(mycut)  # 通过“广播”形式分词，加快速度。

data2 = data2[0].apply(mycut)

data1.to_csv(outputfile1, index=False, header=False, encoding='utf-8')  # 保存结果

data2.to_csv(outputfile2, index=False, header=False, encoding='utf-8')
