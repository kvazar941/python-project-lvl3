"""Engine module."""
import logging
import os
import sys
from urllib.parse import urlparse, urlunparse

import requests
from bs4 import BeautifulSoup
from progress.bar import Bar

from loader.file_reader import read_file
from loader.file_writer import write_file

logging.basicConfig(filename='report.log', filemode='w', level=logging.INFO)

TEXT_IMG = 'Downloading images'
TEXT_LINKS = 'Downloading links'
TEXT_SCRIPTS = 'Downloading scripts'


def rename(name):
    """
    Convert a format to a format.

    'https://ru.hexlet.io/courses' to 'ru-hexlet-io-courses'.

    Args:
        name: str

    Returns:
        str
    """
    url = urlparse(name)
    full_way = url.netloc + url.path
    result_way = full_way.replace('.', '-')
    result_way = result_way.replace('/', '-')
    logging.info('message')
    return result_way


def rename_to_html(name):
    return '.'.join([rename(name), 'html'])


def rename_to_dir(name):
    return '_'.join([rename(name), 'files'])


def rename_to_file(dir_, name):
    way, extension = os.path.splitext(name)
    if extension == '':
        current_file_name = rename_to_html(way)
    else:
        current_file_name = rename(way) + extension
    return '/'.join([dir_, current_file_name])


def get_data(link):
    try:
        link_data = requests.get(link)
    except Exception:
        print('The resource "{0}" is not available.'.format(link))
        print('Check the network connection.')
        print('Check availability of the resource or page.')
        print('The program terminates, the page and resource is not loaded.')
        sys.exit(1)
    return link_data


def make_directory(directory):
    try:
        if os.path.exists(directory):
            logging.info('directory found!')
        else:
            logging.info('created directory!')
            os.mkdir(directory)
    except Exception:
        print("Cannot create directory '{0}'.".format(directory))
        print('Check the permissions on the path to the directory.')
        print("If it's a network drive,")
        print('check if the drive is accessible over the network.')
        print('The program terminates, the page and resource is not loaded.')
        sys.exit(1)


def restore_links(url, links):
    res_link = []
    urla = urlparse(url)
    for link in links:
        urlb = urlparse(link)
        urlb = urlb._replace(scheme=urla.scheme, netloc=urla.netloc)
        res_link.append(urlunparse(urlb))
    return res_link


def get_link_from_tag(content_html, source, tag, netloc):
    soup = BeautifulSoup(content_html, 'html.parser')
    links = [atr[source] for atr in soup.find_all(tag) if atr.get(source)]
    list_result = []
    for link in links:
        if urlparse(link).netloc == netloc:
            list_result.append(link)
        if urlparse(link).netloc == '':
            list_result.append(link)
    return list_result


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

    def get_netloc(self):
        return urlparse(self.url).netloc

    def response(self):
        return get_data(self.url)

    def content_url(self):
        return self.response().text

    def links_img(self):
        return get_link_from_tag(self.content_url(), 'src', 'img', self.get_netloc())

    def links_link(self):
        return get_link_from_tag(self.content_url(), 'href', 'link', self.get_netloc())

    def links_script(self):
        return get_link_from_tag(self.content_url(), 'src', 'script', self.get_netloc())


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
        full_way = rename_to_file(directory, link)
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


def download_source(list_links, url, dir_, progress_text, content_html):
    if list_links:
        a = []
        for link in list_links: 
            if urlparse(link).netloc == urlparse(url).netloc:
                a.append(link)
        links = restore_links(url, a)
        replased_data = get_sourses(links, dir_, progress_text)
        return changed_link(replased_data, content_html)


def load_one_page(url, way):
    page = Page(url)
    dir_ = way + rename_to_dir(page.url)
    text_page = page.content_url()
    download_source(page.links_img(), url, dir_, TEXT_IMG, text_page)
    download_source(page.links_link(), url, dir_, TEXT_LINKS, text_page)
    download_source(page.links_script(), url, dir_, TEXT_SCRIPTS, text_page)
    way_to_html = ''.join([way, page.valid_name()])
    download_html(way_to_html, text_page)
    return str(way_to_html)


def page_load(url_page, way_to_dir):
    return load_one_page(url_page, way_to_dir)
