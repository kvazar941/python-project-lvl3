"""FIle writer module."""


def write(way, content):
    with open('./ru-hexlet-io-courses.html', 'w+') as file_name:
        file_name.write(content)
