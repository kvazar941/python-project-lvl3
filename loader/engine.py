"""Engine module."""
import requests
from loader.file_writer import write

test_page = 'https://ru.hexlet.io/courses'

def page_load():
    r = requests.get(test_page)
    file_name = r.url
    write(file_name, r.text)
    return str(r)

