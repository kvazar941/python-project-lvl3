"""FIle writer module."""


def write(way_to_file, content, mode='w+'):
    with open(way_to_file, mode) as file_name:
        file_name.write(content)
