#!/usr/bin/env/python3
"""Module page_loader."""
import sys

from page_loader.cli import argument_handing
from page_loader.engine import download


def main():
    args = argument_handing()
    try:
        print(download(args.url_page, args.output))
    except FileNotFoundError as fnfe:
        print(fnfe)
        sys.exit(1)
    except PermissionError as pe:
        print(pe)
        sys.exit(1)
    except NotADirectoryError as nade:
        print(nade)
        sys.exit(1)
    except FileExistsError as fee:
        print(fee)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
