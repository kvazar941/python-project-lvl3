"""engine module."""
import os
from pathlib import Path
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


def parse(html, url):
    """
    Parse and changed the html and get list resources for download.

    Args:
        html: str
        url: str

    Returns:
        str, list
    """
    soup = BeautifulSoup(html, 'html.parser')
    original_url = urlparse(url)
    scheme_url = original_url.scheme
    netloc_url = original_url.netloc
    name_directory = make_name_dir(url)
    tags = soup.find_all(TAGS.keys())
    list_replased = []
    for tag in tags:
        link = tag.get(TAGS[tag.name])
        if urlparse(link).netloc in {netloc_url, ''}:
            log_debug(f'Link "{link}" found')
            parsed_link = urlparse(link)
            billet = parsed_link._replace(scheme='', netloc=netloc_url)
            local_link = make_name_file(name_directory, urlunparse(billet))
            tag[TAGS[tag.name]] = local_link
            new_link = parsed_link._replace(scheme=scheme_url, netloc=netloc_url)  # noqa E501
            list_replased.append(urlunparse(new_link))
            log_debug(f'New link: "{new_link}".')
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


def download(url, way=DEFAULT_WAY):
    """
    Load the page and its resources.

    Args:
        url: str
        way: str

    Returns:
        str
    """
    log_info('Program launch.')
    log_info("The download url was obtained: '{0}'".format(url))
    check_way(way)
    html = get_text(url)
    final_html, filtered_links = parse(html, url)
    way_to_file_html = Path(way).joinpath(make_name_html(url))
    if filtered_links:
        directory_sourses = make_full_path_dir(url, way)
        get_sourses(filtered_links, directory_sourses)
    save_html(way_to_file_html, final_html)
    log_debug('Program shutdown.')
    return str(way_to_file_html)
