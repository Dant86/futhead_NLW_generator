from nlw_generator.config import HTML_PARSER, FUTHEAD_URL, SPAN, CLASS, PGS_CLS, DIV, PLAYER_CLS, FUTHEAD_NO_PLATFORM_URL, PLAYER_NAME, STRONG, CLUB_LEAGUE_INFO, NAME, POSITION, LEAGUE, CLUB, ARG, BETTER_ARG, BUGGY_ARGENTINA_CLUBS, SERIE_B_CLUBS, SERIE_B, CHILE, CHILE_CLUBS
from bs4 import BeautifulSoup
from requests import get
from pandas import DataFrame


def get_list_pages():
    resp = get(FUTHEAD_URL)
    raw_html = resp.text
    body = BeautifulSoup(raw_html, HTML_PARSER)
    pages = body.find(SPAN, {CLASS: PGS_CLS})
    pgs_txt = pages.text.replace(' ', '').replace('\n', '')
    pg_num = int(pgs_txt[pgs_txt.index('of') + 2:])
    return pg_num


def extract_player_info(domitem):
    d = {}
    d[NAME] = domitem.find(SPAN, {CLASS: PLAYER_NAME}).text
    clinfo = domitem.find(SPAN, {CLASS: CLUB_LEAGUE_INFO})
    cl = clinfo.text.replace('\n', '').split('|')
    cl = tuple(map(lambda x: x.strip(), cl))
    print(d[NAME])
    print(cl)
    if len(cl) == 1:
        return {}
    if cl[1] in BUGGY_ARGENTINA_CLUBS:
        pos = cl[0]
        club = cl[1]
        league = BETTER_ARG
    elif cl[1] in SERIE_B_CLUBS:
        pos = cl[0]
        club = cl[1]
        league = SERIE_B
    elif cl[1] in CHILE_CLUBS:
        pos = cl[0]
        club = cl[1]
        league = CHILE
    elif cl[2] == ARG:
        (pos, club, _) = cl
        league = BETTER_ARG
    else:
        (pos, club, league) = cl
    d[POSITION] = pos
    d[LEAGUE] = league
    d[CLUB] = club
    return d


def pull_players():
    num_pages = get_list_pages()
    pls = []
    for page_num in range(1, num_pages + 1):
        with_page = f'{FUTHEAD_NO_PLATFORM_URL}{page_num}'
        resp = get(with_page)
        body = BeautifulSoup(resp.text, HTML_PARSER)
        players = body.findAll(DIV, {CLASS: PLAYER_CLS})
        pls += list(map(extract_player_info, players))
    return DataFrame(pls)

