#!/usr/bin/env/python3
"""Module page_loader."""
from page_loader.cli import argument_handing
from page_loader.engine import download


def main():
    args = argument_handing()
    download_result = download(args.url_page, args.output)
    print("Page was downloaded as '{0}'".format(download_result))


if __name__ == '__main__':
    main()
