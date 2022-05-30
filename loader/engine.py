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


def page_load(url_page, way_to_dir):
    page = Page(url_page)
    #write(''.join([way_to_dir, page.valid_name()]), page.content_url())
    soup = BeautifulSoup(page.content_url(), 'html.parser')
    link = [x['src'] for x in soup.find_all('img')]
    #print(soup.find_all('img'))
    print(link)
    return str(way_to_dir + page.valid_name())

