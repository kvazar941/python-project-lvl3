"""cli module."""
import argparse

HELP = 'set downloading page'


def argument_handing():
    """
    Create a parser with the necessary arguments for the application to work.

    Returns:
        parser
    """
    parser = argparse.ArgumentParser(description='Load page')
    parser.add_argument('url_page')
    parser.add_argument('-o', '--output', default='./', help=HELP)
    return parser.parse_args()
