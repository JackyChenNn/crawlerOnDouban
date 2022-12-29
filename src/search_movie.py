import urllib.request
import requests, re
from bs4 import BeautifulSoup

def getid(movie_name):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",}
    params = {"q": movie_name}
    # enter your url
    search_url = "https://www.douban.com/search"
    r = requests.get(search_url, params=params, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    first_movie = soup.find('a', {'class': 'nbg'})['onclick']
    pattern = re.compile('\d{4,}')
    # to str
    id = str(pattern.search(first_movie).group())
    return(id)

'''Debug'''
if __name__ == '__main__':
    print(getid('十二怒汉'))