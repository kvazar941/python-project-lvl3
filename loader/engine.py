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


def changed_link(old_link, new_link, content):
    return content.replace(old_link, new_link)


def make_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

def get_link_from_tag(content, resource, tag):
    soup = BeautifulSoup(content, 'html.parser')
    return [item[resource] for item in soup.find_all(tag) if item.get(resource)!= None]


class Page():
    def __init__(self, url):
        self.url = url

    def valid_name(self):
        return rename_to_html(self.url)

    def response(self):
        return requests.get(self.url)

    def content_url(self):
        return self.response().text

    def links_img(self):
        return get_link_from_tag(self.content_url(), 'src', 'img')
        soup = BeautifulSoup(self.content_url(), 'html.parser')
        return [x['src'] for x in soup.find_all('img')]

    def links_link(self):
        return get_link_from_tag(self.content_url(), 'href', 'link')

    def links_script(self):
        return get_link_from_tag(self.content_url(), 'src', 'script')


def download_file(link, way):
    write(way, get_data(link), 'wb')


def download_html(way_to_file, cont):
    write(way_to_file, cont)


def download_resourses(list_, dir_):
    result = {}
    make_directory(dir_)
    for link in list_:
        full_way = rename_to_image(dir_, link)
        download_file(link, full_way)
        result[link] = full_way
    return result


def load_one_page(url, way):
    page = Page(url)
    dir_ = rename_to_dir(page.url)
    way_to_html = ''.join([way, page.valid_name()])
    content_result = page.content_url()
    a = download_resourses(page.links_img(), dir_)
    b = download_resourses(page.links_link(), dir_)
    c = download_resourses(page.links_script(), dir_)
    for link in a:
        content_result = changed_link(link, a[link], content_result)
    for link in b:
        content_result = changed_link(link, b[link], content_result)
    for link in c:
        content_result = changed_link(link, c[link], content_result)
    download_html(way_to_html, content_result)
    return way_to_html


def page_load(url_page, way_to_dir):
    load_one_page(url_page, way_to_dir)
    return str(rename_to_html(url_page))

