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


def restore_full_link(link, short_link):
    urla = urlparse(link)
    urlb = urlparse(short_link)
    return urlb._replace(scheme=urla.scheme, netloc=urla.netloc)


def restore_all_links(url, links):
    return [urlunparse(restore_full_link(url, link)) for link in links]


def get_sourses(list_links, directory, text_progress):
    dict_changed_links = {}
    make_directory(directory)
    with Bar(text_progress, max=len(list_links)) as progress_bar:
        for link in list_links:
            full_way = rename_to_file(directory, link)
            download_file(link, full_way)
            dict_changed_links[link] = full_way
            progress_bar.next()
    return dict_changed_links


def changed_link(dict_, content_html):
    new_content = content_html
    for link in dict_:
        new_content = new_content.replace(link, dict_[link])
    return new_content


def get_source_one_type(list_links, url, dir_, progress_text, content_html):
    netloc = urlparse(url).netloc
    if list_links:
        link = filter(lambda link: urlparse(link).netloc == netloc, list_links)
        links = restore_all_links(url, link)
        replased_data = get_sourses(links, dir_, progress_text)
        return changed_link(replased_data, content_html)


def load_one_page(url, way):
    page = Page(url)
    dir_ = way + rename_to_dir(page.url)
    text_page = page.content_url()
    get_source_one_type(page.links_img(), url, dir_, TEXT_IMG, text_page)
    get_source_one_type(page.links_link(), url, dir_, TEXT_LINKS, text_page)
    get_source_one_type(page.links_script(), url, dir_, TEXT_SCRIPT, text_page)
    way_to_html = ''.join([way, page.valid_name()])
    download_html(way_to_html, text_page)
    return str(way_to_html)


def page_load(url_page, way_to_dir):
    log('test')
    return load_one_page(url_page, way_to_dir)
