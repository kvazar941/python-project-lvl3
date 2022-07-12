"""engine module."""
import os
from urllib.parse import urlparse, urlunparse

from progress.bar import Bar

from page_loader.checker import check_way
from page_loader.data_recipient import get_data
from page_loader.downloader import download_file, download_html, make_directory
from page_loader.logger import log_debug, log_info
from page_loader.page_object import get_links
from page_loader.renamer import rename_to_dir, rename_to_file, rename_to_html

DEFAULT_WAY = os.getcwd()


def get_full_link(url, short_link):
    url_link = urlparse(url)
    url_short = urlparse(short_link)
    return url_short._replace(scheme=url_link.scheme, netloc=url_link.netloc)


def restore_links(url, links):
    return [urlunparse(get_full_link(url, link)) for link in links]


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
            download_file(link, rename_to_file(directory, link))
            log_debug('File "{0}" download.'.format(link))
            progress_bar.next()
    source = '\n'.join(list_links)
    log_info('The following resources have been uploaded: {0}'.format(source))
    log_debug('Get_sourses complete.')


def changed_link(dict_changed, content_html):
    """
    Replace the links in the html content with local ones.

    Args:
        dict_changed: dict
        content_html: str

    Returns:
        str
    """
    new_content = content_html
    for link in dict_changed:
        new_content = new_content.replace(link, dict_changed[link])
    return new_content


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
    page = get_data(url)
    netloc = urlparse(url).netloc
    
    page_directory = rename_to_dir(url)
    way_html = '/'.join([way, rename_to_html(url)])
    directory_sourses = '/'.join([way, page_directory])
    all_link = get_links(page.text, netloc)
    full_links = restore_links(url, all_link)
    replased_link = {}
    if full_links:
        for link_new, link_old in zip(full_links, all_link):
            replased_link[link_old] = rename_to_file(page_directory, link_new)
        get_sourses(full_links, directory_sourses)
    log_info('Download html, way: {0}.'.format(way_html))
    download_html(way_html, changed_link(replased_link, page.text))
    log_debug('Html downloaded.')
    log_debug('Loaded one page.')
    return str(way_html)


def download(url, way=DEFAULT_WAY):
    log_info('Program launch.')
    log_info("The download url was obtained: '{0}'".format(url))
    check_way(way)
    work_result = load_one_page(url, way)
    log_debug('Program shutdown.')
    return work_result
