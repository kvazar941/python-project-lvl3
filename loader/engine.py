"""engine module."""
from urllib.parse import urlparse, urlunparse

from progress.bar import Bar

from loader.downloader import download_file, download_html, make_directory
from loader.logger import log
from loader.page_object import Page
from loader.renamer import rename_to_dir, rename_to_file

TEXT_IMG = 'Downloading images'
TEXT_LINKS = 'Downloading links'
TEXT_SCRIPT = 'Downloading scripts'


def get_full_link(link, short_link):
    url_link = urlparse(link)
    url_short = urlparse(short_link)
    return url_short._replace(scheme=url_link.scheme, netloc=url_link.netloc)


def restore_all_links(url, links):
    return list(map(lambda link: urlunparse(get_full_link(url, link)), links))


def get_sourses(list_links, directory, text_progress):
    """
    Download resources by links and return the dictionary with changed links.

    Args:
        list_links: list
        directory: str
        text_progress: str

    Returns:
        dict
    """
    make_directory(directory)
    with Bar(text_progress, max=len(list_links)) as progress_bar:
        for link in list_links:
            download_file(link, rename_to_file(directory, link))
            progress_bar.next()
    return {link2: rename_to_file(directory, link2) for link2 in list_links}


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


def filter_links(list_links, url, dir_, progress_text, content_html):
    if list_links:
        netloc = urlparse(url).netloc
        link = filter(lambda link: urlparse(link).netloc == netloc, list_links)
        links = restore_all_links(url, link)
        replased_data = get_sourses(links, dir_, progress_text)
        return changed_link(replased_data, content_html)


def load_one_page(url, way):
    page = Page(url)
    dir_ = way + rename_to_dir(page.url)
    text_page = page.content_url()
    filter_links(page.links_img(), url, dir_, TEXT_IMG, text_page)
    filter_links(page.links_link(), url, dir_, TEXT_LINKS, text_page)
    filter_links(page.links_script(), url, dir_, TEXT_SCRIPT, text_page)
    way_to_html = ''.join([way, page.valid_name()])
    download_html(way_to_html, text_page)
    return str(way_to_html)


def page_load(url_page, way_to_dir):
    log('program launch')
    work_result = load_one_page(url_page, way_to_dir)
    log('program shutdown')
    return work_result
