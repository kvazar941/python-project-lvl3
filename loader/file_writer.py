"""FIle writer module."""


def write(way_to_file, content):
    with open(way_to_file, 'w+') as file_name:
        file_name.write(content)
