"""Engine module."""
#import os
import requests
from loader.file_writer import write


class Page():
    def __init__(self, url):
        self.url = url

    def valid_name(self):
        '''https://ru.hexlet.io/courses --> ru-hexlet-io-courses.html'''
        one = (self.url).split('//')[1]
        two = one.replace('.', '-')
        three = two.replace('/', '-')
        file_name = three + '.html' if three[-4:] != 'html' else three
        return file_name

    def response(self):
        return requests.get(self.url)

    def content_url(self):
        return self.response().text


def page_load(url_page, way_to_dir):
    page = Page(url_page)
    write(way_to_dir + page.valid_name(), page.content_url())
    return '<Response [200]>'

