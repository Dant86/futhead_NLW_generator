from bs4 import BeautifulSoup
from requests import get

PLATFORM = 'xb'
FUTHEAD_URL=f'https://www.futhead.com/21/players/?bin_platform={PLATFORM}'

HTML_PARSER = 'parser.html'
