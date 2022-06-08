"""Engine module."""
import logging
import os

import requests
from bs4 import BeautifulSoup
from progress.bar import Bar

from loader.file_reader import read_file
from loader.file_writer import write_file

logging.basicConfig(filename='report.log', filemode='w', level=logging.INFO)

Progress_img = 'Downloading images'
Progress_links = 'Downloading links'
Progress_scripts = 'Downloading scripts'


def rename(name):
    """
    Convert a format to a format.

    'https://ru.hexlet.io/courses' to 'ru-hexlet-io-courses'.

    Args:
        name: str

    Returns:
        str
    """
    one = name.split('//')[1]
    two = one.replace('.', '-')
    three = two.replace('/', '-')
    logging.info('message')
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
    return requests.get(link)


def make_directory(directory):
    if os.path.exists(directory):
        logging.info('directory found!')
    else:
        logging.info('created directory!')
        os.mkdir(directory)


def get_link_from_tag(content_html, source, tag):
    soup = BeautifulSoup(content_html, 'html.parser')
    return [atr[source] for atr in soup.find_all(tag) if atr.get(source)]


class Page():
    """
    Page.

    Args:
        name: str

    Returns:
        str
    """

    def __init__(self, url):
        """
        Init.

        Args:
            url: str

        Returns:
           str
        """
        self.url = url

    def valid_name(self):
        return rename_to_html(self.url)

    def response(self):
        return get_data(self.url)

    def content_url(self):
        return self.response().text

    def links_img(self):
        return get_link_from_tag(self.content_url(), 'src', 'img')

    def links_link(self):
        return get_link_from_tag(self.content_url(), 'href', 'link')

    def links_script(self):
        return get_link_from_tag(self.content_url(), 'src', 'script')


def download_file(link, way_to_file):
    if os.path.exists(way_to_file):
        if get_data(link).content == read_file(way_to_file, 'rb'):
            return
    write_file(way_to_file, get_data(link).content, 'wb')


def download_html(way_to_file, cont):
    if os.path.exists(way_to_file):
        if cont == read_file(way_to_file, 'rb'):
            return
    write_file(way_to_file, cont)


def get_sourses(list_links, directory, text_progress):
    dict_changed_links = {}
    make_directory(directory)
    progress_bar = Bar(text_progress, max=len(list_links))
    for link in list_links:
        full_way = rename_to_image(directory, link)
        download_file(link, full_way)
        dict_changed_links[link] = full_way
        progress_bar.next()
    progress_bar.finish()
    return dict_changed_links


def changed_link(dict_, content_html):
    new_content = content_html
    for link in dict_:
        new_content = new_content.replace(link, dict_[link])
    return new_content


def load_one_page(url, way):
    page = Page(url)
    dir_ = rename_to_dir(page.url)
    content_result = page.content_url()
    #  loading resources and changing links to img
    replased_img = get_sourses(page.links_img(), dir_, Progress_img)
    content_result = changed_link(replased_img, content_result)
    #  loading resources and changing links to link
    replased_links = get_sourses(page.links_link(), dir_, Progress_links)
    content_result = changed_link(replased_links, content_result)
    #  loading resources and changing links to scripts
    replased_scripts = get_sourses(page.links_script(), dir_, Progress_scripts)
    content_result = changed_link(replased_scripts, content_result)
    #  write the final ~.html to the hard drive
    way_to_html = ''.join([way, page.valid_name()])
    download_html(way_to_html, content_result)
    return str(way_to_html)


def page_load(url_page, way_to_dir):
    return load_one_page(url_page, way_to_dir)
