"""FIle writer module."""
import sys


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
    except Exception:
        print("Cannot create file '{0}' at the specified path.".format(way))
        print('Check the permissions on the path to the file.')
        print("If it's a network drive,")
        print('check if the drive is accessible over the network.')
        print('The program terminates.')
        print('The page and resource is not loaded.')
        sys.exit(1)
