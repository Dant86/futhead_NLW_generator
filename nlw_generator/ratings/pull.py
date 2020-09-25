from nlw_generator.config import HTML_PARSER, FUTHEAD_URL, SPAN, CLASS, PGS_CLS
from bs4 import BeautifulSoup
from requests import get

def get_list_pages():
    resp = get(FUTHEAD_URL)
    raw_html = resp.text
    body = BeautifulSoup(raw_html, HTML_PARSER)
    pages = body.find(SPAN, {CLASS: PGS_CLS})
    pgs_txt = pages.text.replace(' ', '').replace('\n', '')
    pg_num = int(pgs_txt[pgs_txt.index('of') + 2:])
    return pg_num

