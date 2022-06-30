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
    parser.add_argument('-o', '--output', default='./', help=HELP)
    parser.add_argument('url_page')
    return parser.parse_args()
