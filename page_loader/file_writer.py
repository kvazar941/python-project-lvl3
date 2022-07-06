"""FIle writer module."""
import logging

ERROR = "Cannot create file '{0}' at the specified path."


def write_file(way, content_file, mode='w+'):
    """
    Write file.

    Args:
        way: str
        content_file: any
        mode: str
    """
    try:
        with open(way, mode) as file_name:
            file_name.write(content_file)
    except FileNotFoundError:
        logging.info(ERROR.format(way))
        raise FileNotFoundError(ERROR.format(way))
