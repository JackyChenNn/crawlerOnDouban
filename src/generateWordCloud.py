#!/usr/bin/env python
# coding: utf-8

import jieba
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image
from collections import Counter
import matplotlib.pyplot as plt

def wordCloud():
    comments_path = "./12AngryMan_Comments.txt"
    with open(comments_path,"r",encoding="utf-8") as f:
        content = f.read()

    res_list = [i for i in jieba.cut(content) if len(i)>=2]
    # 打印分词结果
    # print(res_list)

    # 输出图片
    plt.imshow(wc)
    plt.axis("off")   # 去掉坐标轴
    plt.show()

    # 生成词云
    wc = WordCloud(width=800,  # 词云图宽
                   height=800, # 词云图高
                   background_color='white', # 词云图背景颜色，默认为白色
                   font_path='/Users/chenhaodong/Library/Fonts/PingFang.ttc',  # 词云图 字体（中文需要设定为本机有的中文字体）
                  ) # 返回一个词云对象
                  
    print(wc)
    wc.generate(" ".join(res_list))
    # 保存词云图片
    wc.to_file("12Angryman.jpg")