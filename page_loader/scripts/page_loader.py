#!/usr/bin/env/python3
"""Module page_loader."""
from page_loader.cli import argument_handing
from page_loader.engine import page_load


def download():
    args = argument_handing()
    print(page_load(args.url_page, args.output))


if __name__ == '__main__':
    download()
