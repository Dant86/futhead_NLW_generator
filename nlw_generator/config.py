from bs4 import BeautifulSoup
from requests import get

# URL details
PLATFORM = 'xb'
FUTHEAD_URL=f'https://www.futhead.com/21/players/?bin_platform={PLATFORM}'

# Parsing constants
HTML_PARSER = 'html.parser'
SPAN = 'span'
CLASS = 'class'
PGS_CLS = 'font-12 font-bold margin-l-r-10'




