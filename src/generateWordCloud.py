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
    # print(res_list)

    # output image
    plt.imshow(word_cloud)
    # Remove the axis
    plt.axis("off")   
    plt.show()

    # generate word cloud
    word_cloud = WordCloud(width=800,
                   height=800,
                   background_color='white',
                   font_path='/Users/chenhaodong/Library/Fonts/PingFang.ttc',
                  )
                  
    print(word_cloud)
    word_cloud.generate(" ".join(res_list))
    # Save Word Cloud Image
    word_cloud.to_file("MovieCommentsWordcloud.jpg")