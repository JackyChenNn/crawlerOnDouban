import requests
from lxml import etree
import random
import time
from bs4 import BeautifulSoup
from search_movie import getid
import re

def crawlerOnComments(url, movie_id, times, cookies=None):
    # add the header information to modify the real browser
    my_headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

    # If it is still recognized as not a browser, you need to add more header information
    if cookies == None:
        r = requests.get(url, headers=my_headers)
    else:
        r = requests.get(url, headers=my_headers, cookies=cookies)

    if r.status_code == 200 and times == 0:
        print("Successful connected with Douban.")

    # Get the specific content of the server response
    selector = etree.HTML(r.text)

    # Processing comment
    temp = selector.xpath('//div[@class="comment"]')

    with open("./Movie_Star.txt", "a+", encoding='utf-8') as f, open("./Movie_Comments.txt", "a+", encoding='utf-8') as f2:
        for everyElement in temp:
            # userName = everyElement.xpath('./h3/span[@class="comment-info"]/a/text()')
            userStar = everyElement.xpath('./h3/span[@class="comment-info"]/span[2]/@class')
            userComment = everyElement.xpath('./p/span[@class="short"]/text()')

            # Add a rating of 0 if the user review contains no stars
            if not userStar:
                userStar = ["allstar0 rating"]

            AngryMan_Comments = f"{userComment}\n"
            AngryMan_Star = f"{userStar}\n"
            f.write(AngryMan_Star)
            f2.write(AngryMan_Comments)

    # How to determine it's the last page
    # //div[@id="paginator"]/span[1]
    # //div[@id="paginator"]/a/text() includes “后页”

    if "后页 >" in selector.xpath('//div[@id="paginator"]/a/text()'):
        newTimes = times + 1
        newPage = newTimes * 20
        newUrl = 'https://movie.douban.com/subject/' + movie_id + '/comments?start='+ str(newPage) +'&limit=20&status=P&sort=new_score'
        print('Page ' + str(newTimes) + ' crawling')
        print("Spider on: " + newUrl + '\n')
        # Recursively crawl the content of the next page
        crawlerOnComments(newUrl, movie_id, newTimes)
    else:
        print('Crawling completed!')
        