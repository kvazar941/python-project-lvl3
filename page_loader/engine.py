"""engine module."""
import os
from urllib.parse import urlparse, urlunparse

from bs4 import BeautifulSoup
from progress.bar import Bar

from page_loader.checker import check_way
from page_loader.data_recipient import get_text
from page_loader.downloader import download_file, download_html, make_directory
from page_loader.logger import log_debug, log_info
from page_loader.name_maker import (make_full_path_dir, make_name_dir,
                                    make_name_file, make_name_html)

DEFAULT_WAY = os.getcwd()
TAGS = {'img': 'src', 'link': 'href', 'script': 'src'}


def get_changed_html(url):
    html = get_text(url)
    soup = BeautifulSoup(html, 'html.parser')
    netloc_url = urlparse(url).netloc
    scheme_url = urlparse(url).scheme
    tags = soup.find_all(TAGS.keys())
    list_replased = []
    for tag in tags:
        link = tag.get(TAGS[tag.name])
        if urlparse(link).netloc in {netloc_url, ''}:
            new = f'{netloc_url}{urlparse(link).path}'
            local_link = make_name_file(make_name_dir(url), new)
            tag[TAGS[tag.name]] = local_link
            new_link = urlparse(link)
            new_link._replace(scheme=scheme_url, netloc=netloc_url)
            list_replased.append(urlunparse(new_link))
    return soup.prettify(), list_replased


def get_sourses(list_links, directory):
    """
    Download resources by links and return the dictionary with changed links.

    Args:
        list_links: list
        directory: str
    """
    log_debug('Run get_sourses.')
    make_directory(directory)
    with Bar('Progress: ', max=len(list_links)) as progress_bar:
        for link in list_links:
            log_debug('Downloading file "{0}".'.format(link))
            download_file(link, make_name_file(directory, link))
            log_debug('File "{0}" download.'.format(link))
            progress_bar.next()
    source = '\n'.join(list_links)
    log_info('The following resources have been uploaded: {0}'.format(source))
    log_debug('Get_sourses complete.')


def save_html(way, text):
    log_debug('Download html, way: {0}.'.format(way))
    download_html(way, text)
    log_debug('Html downloaded.')
    return str(way)


def load_one_page(url, way):
    """
    Load the page and its resources.

    Args:
        url: str
        way: str

    Returns:
        str
    """
    log_debug('Run load one page.')
    final_html, all_links = get_changed_html(url)
    directory_sourses = make_full_path_dir(url, way)
    way_to_file_html = f'{way}/{make_name_html(url)}'
    if all_links:
        get_sourses(all_links, directory_sourses)
    log_debug('Loaded one page.')
    return save_html(way_to_file_html, final_html)


def download(url, way=DEFAULT_WAY):
    log_info('Program launch.')
    log_info("The download url was obtained: '{0}'".format(url))
    check_way(way)
    work_result = load_one_page(url, way)
    log_debug('Program shutdown.')
    return work_result
