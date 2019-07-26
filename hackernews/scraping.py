import requests
from bs4 import BeautifulSoup


class Parser:

    def __init__(self):
        self.link = []
        self.title = []
        self.result = []

    def get_html(self, url):
        r = requests.get(url)
        return r.text

    def get_all_links(self):
        soup = BeautifulSoup(self.get_html('http://akipress.org/'), 'lxml')
        ads = soup.findAll('a', class_="newslink")

        for ad in ads:
            try:
                self.link.append(ad.get('href'))
            except:
                print('False link')
            try:
                self.title.append(ad.get_text())
            except:
                print('False text')

            result2 = {
                'link': self.link,
                'title': self.title,
            }

