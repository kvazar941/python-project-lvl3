#!/usr/bin/env/python3
"""Module page_loader."""
import logging
import sys

from page_loader.cli import argument_handing
from page_loader.engine import download


def main():
    args = argument_handing()
    try:
        print(download(args.url_page, args.output))
    except Exception:
        logging.info('Error')
        sys.exit(1)
    else:
        logging.info('Done')
        sys.exit(0)


if __name__ == '__main__':
    main()
