"""Engine module."""
#import os
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests
from loader.file_writer import write


def rename(name):
    '''https://ru.hexlet.io/courses --> ru-hexlet-io-courses'''
    one = name.split('//')[1]
    two = one.replace('.', '-')
    return two.replace('/', '-')


def rename_to_html(name):
    res_name = rename(name)
    return res_name + '.html' if res_name[-4:] != 'html' else res_name


def rename_to_png(name):
    res_name = rename(name)
    return res_name + '.png' if res_name[-3:] != 'png' else res_name


class Page():
    def __init__(self, url):
        self.url = url

    def valid_name(self):
        '''https://ru.hexlet.io/courses --> ru-hexlet-io-courses.html'''
        return rename_to_html(self.url)

    def response(self):
        return requests.get(self.url)

    def content_url(self):
        return self.response().text

    def links(self):
        self.soup = BeautifulSoup(self.content_url(), 'html.parser')
        return [x['src'] for x in self.soup.find_all('img')]


def page_load(url_page, way_to_dir):
    page = Page(url_page)
    down_dir = ''.join([way_to_dir, page.valid_name()])
    cont = page.content_url()
    print(page.links())
    for a in page.links():
        r = requests.get(a)
        with open('./downloads/1.svg', 'wb') as file_:
            file_.write(r.content)
        new_cont = cont.replace(a, './downloads/1.svg')
    write(down_dir, new_cont)
    return str(way_to_dir + page.valid_name())

