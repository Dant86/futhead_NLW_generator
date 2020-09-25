from nlw_generator.config import HTML_PARSER, FUTHEAD_URL
from bs4 import BeautifulSoup
from requests import get

def get_list_pages():
    resp = get(FUTHEAD_URL)
    raw_html = resp.text
    body = BeautifulSoup(raw_html, HTML_PARSER)
    print(body)

