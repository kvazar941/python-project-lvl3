"""engine module."""
import os
from urllib.parse import urlparse

from progress.bar import Bar

from page_loader.checker import check_way
from page_loader.data_recipient import get_data
from page_loader.downloader import download_file, download_html, make_directory
from page_loader.filters_links import filter_links, restore_links
from page_loader.logger import log_debug, log_info
from page_loader.name_maker import (make_full_path_dir, make_name_dir,
                                    make_name_file, make_name_html)

DEFAULT_WAY = os.getcwd()


def get_replased_link(full_links, all_link, url):
    replased_link = {}
    for link_new, link_old in zip(full_links, all_link):
        replased_link[link_old] = make_name_file(make_name_dir(url), link_new)
    return replased_link


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


def save_html(way, url, text):
    log_debug('Download html, way: {0}.'.format(way))
    way_to_file_html = '/'.join([way, make_name_html(url)])
    download_html(way_to_file_html, text)
    log_debug('Html downloaded.')
    return str(way_to_file_html)


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
    directory_sourses = make_full_path_dir(url, way)
    all_link = filter_links(page.text, urlparse(url).netloc)
    full_links = restore_links(url, all_link)
    dict_replased = {}
    if full_links:
        dict_replased = get_replased_link(full_links, all_link, url)
        get_sourses(full_links, directory_sourses)
    log_debug('Loaded one page.')
    return save_html(way, url, changed_link(dict_replased, page.text))


def download(url, way=DEFAULT_WAY):
    log_info('Program launch.')
    log_info("The download url was obtained: '{0}'".format(url))
    check_way(way)
    work_result = load_one_page(url, way)
    log_debug('Program shutdown.')
    return work_result
