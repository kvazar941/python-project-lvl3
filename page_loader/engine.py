"""engine module."""
import logging
import os
from urllib.parse import urlparse, urlunparse

import requests
from progress.bar import Bar

from page_loader.downloader import download_file, download_html, make_directory
from page_loader.page_object import Page
from page_loader.renamer import rename_to_dir, rename_to_file

TEXT_IMG = 'Downloading images'
TEXT_LINK = 'Downloading source of links'
TEXT_SCRIPT = 'Downloading source of scripts'
VALID_CODE = 200


def get_full_link(url, short_link):
    url_link = urlparse(url)
    url_short = urlparse(short_link)
    return url_short._replace(scheme=url_link.scheme, netloc=url_link.netloc)


def restore_links(url, links):
    logging.info('run restore_links')
    return [urlunparse(get_full_link(url, link)) for link in links]


def get_sourses(list_links, directory, text_progress):
    """
    Download resources by links and return the dictionary with changed links.

    Args:
        list_links: list
        directory: str
        text_progress: str
    """
    logging.debug('run get_sourses')
    logging.info('create a directory "{0}".'.format(directory))
    make_directory(directory)
    logging.info('directory "{0}" created.'.format(directory))
    with Bar(text_progress, max=len(list_links)) as progress_bar:
        for link in list_links:
            logging.info('downloading file "{0}".'.format(link))
            download_file(link, rename_to_file(directory, link))
            logging.info('file "{0}" download.'.format(link))
            progress_bar.next()
    logging.debug('get_sourses complete.')


def changed_link(dict_changed, content_html):
    """
    Replace the links in the html content with local ones.

    Args:
        dict_changed: dict
        content_html: str

    Returns:
        str
    """
    logging.info('run changed_link')
    new_content = content_html
    for link in dict_changed:
        new_content = new_content.replace(link, dict_changed[link])
    return new_content


def filter_netloc(list_links, url):
    netloc = urlparse(url).netloc
    return filter(lambda link: urlparse(link).netloc == netloc or urlparse(link).netloc == '', list_links)


def load_one_page(url, way):
    """
    Load the page and its resources..

    Args:
        url: str
        way: str

    Returns:
        str
    """
    logging.info('run load one page')
    page = Page(url)
    dir_ = '/'.join([way, rename_to_dir(page.url)])
    texts = [TEXT_IMG, TEXT_LINK, TEXT_SCRIPT]
    lists = [page.links_img(), page.links_link(), page.links_script()]
    for list_, text in zip(lists, texts):
        if list_:
            logging.info(' '.join(list_))
            links = restore_links(page.url, filter_netloc(list_, page.url))
            logging.info(' '.join(links))
            get_sourses(links, dir_, text)
            replased = {link_old: rename_to_file(rename_to_dir(page.url), link_new) for link_new, link_old in zip(links, list_)}
            logging.info(replased)
            print(replased)
    way_to_html = '/'.join([way, page.valid_name()])
    logging.info(f'download_html, way: {way_to_html}')
    download_html(way_to_html, changed_link(replased, page.content_url()))
    logging.info('html downloaded')
    logging.info('loaded one page')
    return str(way_to_html)


def verify_url(url):
    expected_url = requests.get(url)
    if expected_url.status_code != VALID_CODE:
        logging.error('"{0}" is not available.'.format(url))
        raise ConnectionError('"{0}" is not available.'.format(url))
    else:
        logging.error('The url was obtained: "{0}"'.format(url))

        
def verify_way(way):
    if not os.path.exists(way):
        logging.info('The directory {0} does not exist'.format(way))
        raise FileNotFoundError('The directory {0} does not exist'.format(way))
    if way in {'/sys', '/bin', '/tmp'}:
        logging.info('write to directory {0} is not available'.format(way))
        raise OSError('write to directory {0} is not available'.format(way))
    if not os.path.isdir(way):
        logging.info('way {0} is not directory'.format(way))
        raise OSError('way {0} is not directory'.format(way))
    else:
        logging.info('The download path was obtained: "{0}"'.format(way))


def download(url_page, way_to_dir=os.getcwd()):
    logging.info('program launch')
    verify_url(url_page)
    verify_way(way_to_dir)
    work_result = load_one_page(url_page, way_to_dir)
    logging.info('program shutdown')
    return work_result
