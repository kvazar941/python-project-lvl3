"""Engine module."""
import os
from urllib.parse import urlparse
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests
from loader.file_writer import write


def rename(name):
    '''https://ru.hexlet.io/courses --> ru-hexlet-io-courses'''
    one = name.split('//')[1]
    two = one.replace('.', '-')
    three = two.replace('/', '-')
    return three[::-4] if three.endswith('html') else three


def rename_to_html(name):
    return '.'.join([rename(name), 'html'])


def rename_to_dir(name):
    return '_'.join([rename(name), 'files'])


def rename_to_image(dir_, name):
    way, extension = os.path.splitext(name)
    current_file_name = rename(way) + extension
    return '/'.join([dir_, current_file_name])


def get_data(link):
    data = requests.get(link)
    return data.content


def download_file(link, way):
    write(way, get_data(link), 'wb')


def changed_link(old_link, new_link, content):
    return content.replace(old_link, new_link)


def make_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


class Page():
    def __init__(self, url):
        self.url = url

    def valid_name(self):
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
    dir_ = rename_to_dir(page.url)
    make_directory(dir_)
    #if not os.path.exists(dir_):
    #    os.mkdir(dir_)
    for link in page.links():
        full_way = rename_to_image(dir_, link)
        download_file(link, full_way)
        cont = changed_link(link, full_way, cont)
    write(down_dir, cont)
    return str(way_to_dir + page.valid_name())

