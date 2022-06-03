"""FIle writer module."""


def write_file(way_to_file, content_file, mode='w+'):
    """
    Write file.

    Args:
        way_to_file: str
        content_file: any
        mode: str
    """
    with open(way_to_file, mode) as file_name:
        file_name.write(content_file)
