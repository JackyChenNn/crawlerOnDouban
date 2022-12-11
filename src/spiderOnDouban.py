import requests
from lxml import etree
import random
import time

def spiderOnDouban(url, times, cookies=None):
    # Python中典型的字典类型变量
    my_headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

    # 如果还是被识别不是浏览器，则需要添加更多的头部信息
    if cookies == None:
        r = requests.get(url, headers=my_headers)
    else:
        r = requests.get(url, headers=my_headers, cookies=cookies)

    if r.status_code == 200 and times == 0:
        print("Successful connected with Douban.")

    # 整个网页的内容，有一些无用内容需要剔除，在Python中我们也可以找到相关的工具包来处理
    # print(r.text)

    # 取出具体内容
    # from lxml import etree
    selector = etree.HTML(r.text)

    # # 取出内容后，进行更加精确的匹配
    # # 经过对网页源代码的查看，我们选出span标签中class属性为comment-info的，这就是每一页中的所有评论
    # selector.xpath('//span[@class="comment-info"]')
    #
    # # 从中我们选出用户名 即comment-info中 a标签的属性
    # username = selector.xpath('//span[@class="comment-info"]/a/text()')
    # # 测试是否成功取出
    # print(username)
    #
    # # 取出用户评价星级
    # userStar = selector.xpath('//span[@class="comment-info"]/span[2]/@class')
    # print(userStar)
    # # 查看总共有多少个用户评价星级，如果数量同评论数量不等，则有不是逐一对应的情况，需要我们进一步处理
    # print(len(userStar))
    #
    # # 取出文字评价
    # userComment = selector.xpath('//span[@class="short"]/text()')
    # print(userComment)
    # print(len(userComment))
    #
    # # 让提取的数据一一对应
    # # 引入中间值，利用python的序列进行拆分
    # # temp = selector.xpath('//div[@class="comment"]')
    # # print(temp[0])
    # # 查看用户评价是否包含星级
    # # print(temp[3].xpath('./h3/span[2]/span[2]/@class'))
    #
    # # 这里为什么temp是div标签中class属性为comment的？
    # # 是因为我们需要找到一个容器 其中包含了每条评论的所有信息——用户名、评分、评价内容等等
    # temp = selector.xpath('//div[@class="comment"]')
    # # 迭代每一个元素
    # for everyElement in temp:
    #     # 取得相对路径
    #     userName = everyElement.xpath('./h3/span[@class="comment-info"]/a/text()')
    #     userStar = everyElement.xpath('./h3/span[@class="comment-info"]/span[2]/@class')
    #     userComment = everyElement.xpath('./p/span[@class="short"]/text()')
    #
    #     # 如果用户评价不包含星级 则添加评分0
    #     if not userStar:
    #         userStar = ["allstar0 rating"]
    #
    #     print(f"{userName}::{userStar}::{userComment}")

    # 继续处理评论内容
    # 保存到文件做持久化储存
    print(selector.xpath)
    temp = selector.xpath('//div[@class="comment"]')

    with open("./12AngryMan_Short.txt", "a+", encoding='utf-8') as f:
        for everyElement in temp:
            # 取得相对路径
            userName = everyElement.xpath('./h3/span[@class="comment-info"]/a/text()')
            userStar = everyElement.xpath('./h3/span[@class="comment-info"]/span[2]/@class')
            userComment = everyElement.xpath('./p/span[@class="short"]/text()')

            # print(userName)
            # print(userStar)
            # print(userComment)
            # 如果用户评价不包含星级 则添加评分0
            if not userStar:
                userStar = ["allstar0 rating"]

            AngryMan_Short = f"{userName}::{userStar}::{userComment}\n"
            f.write(AngryMan_Short)

    # 问题延伸：怎么翻页？
    # https://movie.douban.com/subject/1293182/comments?percent_type=&start=20&limit=20&status=P&sort=new_score&comments_only=1
    # https://movie.douban.com/subject/1293182/comments?percent_type=&start=40&limit=20&status=P&sort=new_score&comments_only=1
    # 怎么确定是最后一页？
    # //div[@id="paginator"]/span[1]
    # //div[@id="paginator"]/a/text()包含“后页”

    if "后页 >" in selector.xpath('//div[@id="paginator"]/a/text()'):
        newTimes = times + 1
        newPage = newTimes * 20
        newUrl = 'https://movie.douban.com/subject/1293182/comments?start='+ str(newPage) +'&limit=20&status=P&sort=new_score'
        print('Page ' + str(newTimes) + ' crawling')
        print("Spider on: " + newUrl + '\n')
        #递归爬取下一页内容
        spiderOnDouban(newUrl, newTimes)
    else:
        print('Crawling completed!')