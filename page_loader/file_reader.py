"""module file_reader."""


def read_file(way_to_file, mode='r'):
    """
    Read file.

    Args:
        way_to_file: str
        mode: str

    Returns:
        str
    """
    try:
        with open(way_to_file, mode) as file_name:
            file_content = file_name.read()
    except Exception:
        raise OSError('error read file')
    return file_content
