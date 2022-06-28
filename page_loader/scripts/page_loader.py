#!/usr/bin/env/python3
"""Module page_loader."""
from page_loader.cli import argument_handing
from page_loader.engine import download


def main():
    args = argument_handing()
    print(download(args.url_page, args.output))


if __name__ == '__main__':
    main()
