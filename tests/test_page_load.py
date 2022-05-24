"""Test_page_load"""
from loader.engine import page_load

def test_page_load():
    assert page_load() == '<Response [200]>'
