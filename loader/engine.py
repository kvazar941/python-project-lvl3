"""engine module."""
import logging
from urllib.parse import urlparse, urlunparse

from progress.bar import Bar

from loader.downloader import download_file, download_html, make_directory
from loader.page_object import Page
from loader.renamer import rename_to_dir, rename_to_file

logging.basicConfig(filename='report.log', filemode='w', level=logging.INFO)

TEXT_IMG = 'Downloading images'
TEXT_LINKS = 'Downloading links'
TEXT_SCRIPTS = 'Downloading scripts'


def restore_full_link(link, short_link):
    urla = urlparse(link)
    urlb = urlparse(short_link)
    return urlb._replace(scheme=urla.scheme, netloc=urla.netloc)


def restore_all_links(url, links):
    return [urlunparse(restore_full_link(url, link)) for link in links]


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


def download_source(list_links, url, dir_, progress_text, content_html):
    if list_links:
        filtered_list = []
        for link in list_links:
            if urlparse(link).netloc == urlparse(url).netloc:
                filtered_list.append(link)
        links = restore_all_links(url, filtered_list)
        replased_data = get_sourses(links, dir_, progress_text)
        return changed_link(replased_data, content_html)


def changed_link(dict_, content_html):
    new_content = content_html
    for link in dict_:
        new_content = new_content.replace(link, dict_[link])
    return new_content


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
