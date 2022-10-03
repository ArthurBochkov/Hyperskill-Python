import requests
import string
import os

from bs4 import BeautifulSoup

class WebScrapper:

    def __init__(self, pages, types):
        self.names = []
        self.pages = pages
        self.types = types


    def get_file_name(self, name):
        name = name.replace(' ', '_')
        for s in string.punctuation:
            if s != '_':
                name = name.replace(s, '')
        name = name.strip() + '.txt'
        return name


    def make_dir(self, page):
        dir = f'PAGE_{page}'
        if not os.access(dir, os.F_OK):
            os.mkdir(dir)
        for x in os.listdir(dir):
            os.remove(dir + '\\' + x)
        return dir


    def write_file(self, file_name, url):
        self.names.append(file_name)
        f = open(file_name, 'wb')
        rx = requests.get(url)
        soup = BeautifulSoup(rx.content, 'html.parser')
        article_body = soup.find("div", {"class": "c-article-body"}).text.strip()
        f.write(article_body.encode())
        f.close()


    def start(self):
        for page in range(self.pages):
            r = requests.get(f'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page={page+1}')
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, 'html.parser')

                dir = self.make_dir(page + 1)

                articles = soup.find_all('article', {'class': 'u-full-height c-card c-card--flush'})
                for x in articles:
                    if x.find('span', {"class":"c-meta__type"}).text == self.types:
                        tag_a = x.find('a', {'itemprop':'url'})
                        file_name = self.get_file_name(tag_a.text)
                        self.write_file(f'{dir}\\' + file_name, 'https://www.nature.com' + tag_a.get('href'))
            else:
                print(f'The URL returned {r.status_code}')
        print('Saved all articles.', self.names)


if __name__ == '__main__':
    web = WebScrapper(int(input()), input())
    web.start()