"""module file_reader."""

def read(way_to_file):
    """
    Read file.

    Args:
        way_to_file: str

    Returns:
        str
    """
    with open(way_to_file) as file_name:
        file_content = file_name.read()
    return file_content
