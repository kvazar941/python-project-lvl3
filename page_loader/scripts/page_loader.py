#!/usr/bin/env/python3
"""Module page_loader."""
import sys
import logging

from page_loader.cli import argument_handing
from page_loader.engine import download


def main():
    args = argument_handing()
    try:
        print(download(args.url_page, args.output))
    except FileExistsError:
        sys.exit(1)


if __name__ == '__main__':
    main()
