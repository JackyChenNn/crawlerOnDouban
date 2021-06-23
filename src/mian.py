# 需求： 对豆瓣“十二怒汉”电影的评论进行数据抓取分析

import requests

# # 先简单地模拟发送请求 我们会发现服务器并不会返回网站的数据给你
# r = requests.get('https://movie.douban.com/subject/1293182/comments')
#
# # HTTP请求返回状态码418 I'm a teapot
# print(r.status_code)
#
# # 我们会发现返回空值
# print(r.text)


# 如何去模仿一个真正的浏览器？
# 我们需要知道浏览器去访问网站的时候是怎么发送请求的
# 通过HTTP/HTTPS协议
# 比如使用HTTP协议 需要包含请求行 请求头 和请求报文
# 请求行样例： GET /xxx.html HTTP/1.1 (CRLF)
# 包含：    请求方法  URI      协议版本  换行
# 请求报文在GET方法中是没有的 在POST方法中就有

# 需要把需求用Python转换成协议

url = 'https://movie.douban.com/subject/1293182/comments'
my_headers = { }