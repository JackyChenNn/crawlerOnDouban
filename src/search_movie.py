import urllib.request
import requests, re
from bs4 import BeautifulSoup

def getid(name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    }
    movie_name = name
    params = {
        "q": movie_name
    }
    search_url = "https://www.douban.com/search"
    r = requests.get(search_url, params=params, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    first_movie_info = soup.find('a', {'class': 'nbg'})['onclick']
    pattern = re.compile('\d{4,}')
    sid = str(pattern.search(first_movie_info).group())
    return(sid)

'''Debug'''
if __name__ == '__main__':
    print(getid('十二怒汉'))