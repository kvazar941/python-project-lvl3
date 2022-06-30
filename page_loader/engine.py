"""engine module."""
import logging
from urllib.parse import urlparse, urlunparse

from progress.bar import Bar

from page_loader.downloader import download_file, download_html, make_directory
from page_loader.page_object import Page
from page_loader.renamer import rename_to_dir, rename_to_file

TEXT_IMG = 'Downloading images'
TEXT_LINK = 'Downloading source of links'
TEXT_SCRIPT = 'Downloading source of scripts'
ERROR = 'The directory {0} does not exist'


def get_full_link(url, short_link):
    url_link = urlparse(url)
    url_short = urlparse(short_link)
    return url_short._replace(scheme=url_link.scheme, netloc=url_link.netloc)


def restore_links(url, links):
    return [urlunparse(get_full_link(url, link)) for link in links]


def get_sourses(list_links, directory, text_progress):
    """
    Download resources by links and return the dictionary with changed links.

    Args:
        list_links: list
        directory: str
        text_progress: str
    """
    logging.info('create a directory "{0}".'.format(directory))
    make_directory(directory)
    logging.info('directory "{0}" created.'.format(directory))
    with Bar(text_progress, max=len(list_links)) as progress_bar:
        for link in list_links:
            logging.info('downloading file "{0}".'.format(link))
            download_file(link, rename_to_file(directory, link))
            logging.info('file "{0}" download.'.format(link))
            progress_bar.next()


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


def filter_netloc(list_links, url):
    netloc = urlparse(url).netloc
    return filter(lambda link: urlparse(link).netloc == netloc, list_links)


def load_one_page(url, way):
    """
    Load the page and its resources..

    Args:
        url: str
        way: str

    Returns:
        str
    """
    page = Page(url)
    dir_ = ''.join([way, rename_to_dir(page.url)])
    texts = [TEXT_IMG, TEXT_LINK, TEXT_SCRIPT]
    lists = [page.links_img(), page.links_link(), page.links_script()]
    for list_, text in zip(lists, texts):
        if list_:
            links = restore_links(page.url, filter_netloc(list_, page.url))
            get_sourses(links, dir_, text)
            replased = {link: rename_to_file(dir_, link) for link in list_}
            changed_link(replased, page.content_url())
    way_to_html = ''.join([way, page.valid_name()])
    download_html(way_to_html, page.content_url())
    return str(way_to_html)


def download(url_page, way_to_dir):
    logging.info('program launch')
    logging.info('The download path was obtained: "{0}"'.format(way_to_dir))
    try:
        work_result = load_one_page(url_page, way_to_dir)
    except FileNotFoundError:
        logging.info(ERROR.format(way_to_dir))
        raise FileNotFoundError(ERROR.format(way_to_dir))
    logging.info('program shutdown')
    return work_result
