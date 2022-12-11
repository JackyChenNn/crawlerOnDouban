import os
from urllib.request import urlretrieve

class img_operator:
    def __init__(self, selector, path = "imgs/"):
        self.selector = selector
        if(os.path.exists(path) is False):
            os.mkdir(path)
        self.path = path

    def get_movie_poster(self):
        movie_poster_url = self.selector.xpath('//div[@class="movie-summary"]/div[@class="movie-pic"]/a/img/@src')
        movie_poster_title = self.selector.xpath('//div[@class="movie-summary"]/div[@class="movie-pic"]/a/img/@title')
        if movie_poster_url is not None:
            self._download_img(movie_poster_url[0], movie_poster_title[0]+'.jpg')

    def get_avatars(self):
        temp = self.selector.xpath('//div[@class="comment-item "]')
        for every_element in temp:
            user_name = every_element.xpath('./div[@class="comment"]/h3/span[@class="comment-info"]/a/text()')
            user_avatar_url = every_element.xpath('./div[@class="avatar"]/a/img/@src')
            self._download_img(user_avatar_url[0], user_name[0]+'_avatar.jpg')
            
    def _download_img(self, url, filename:str):
        filename = filename.replace('*', '')
        urlretrieve(url, self.path + filename)