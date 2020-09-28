from nlw_generator.config.club_league_constants import ARG, \
                                                       BETTER_ARG, \
                                                       SERIE_B, CHILE, \
                                                       ARG_CLUBS, \
                                                       SERIE_B_CLUBS, \
                                                       CHILE_CLUBS
from nlw_generator.config.dataframe_cols import NAME, POSITION, \
                                                LEAGUE, CLUB, COUNTRY, \
                                                OVR
from nlw_generator.config.url_details import FUTHEAD_URL, \
                                             FUTHEAD_NO_PLATFORM_URL, \
                                             FUTHEAD_BASE_URL, GK_URL
from nlw_generator.config.parsing import HTML_PARSER, SPAN, DIV, \
                                         CLASS, PGS_CLS, PLAYER_CLS, \
                                         PLAYER_NAME, \
                                         CLUB_LEAGUE_INFO, STAT_CLS, \
                                         STAT_VAL_CLS, STAT_TYPE_CLS, \
                                         NATION_CLS, A, LINK_CLS, \
                                         HREF, NATION_IX, RATING_CLS
from bs4 import BeautifulSoup
from pandas import DataFrame, concat
from requests import get


def get_list_pages(url):
    resp = get(url)
    raw_html = resp.text
    body = BeautifulSoup(raw_html, HTML_PARSER)
    pages = body.find(SPAN, {CLASS: PGS_CLS})
    pgs_txt = pages.text.replace(' ', '').replace('\n', '')
    pg_num = int(pgs_txt[pgs_txt.index('of') + 2:])
    return pg_num


def extract_player_info(domitem):
    d = {}
    name = domitem.find(SPAN, {CLASS: PLAYER_NAME}).text
    clinfo = domitem.find(SPAN, {CLASS: CLUB_LEAGUE_INFO})
    cl = clinfo.text.replace('\n', '').split('|')
    cl = tuple(map(lambda x: x.strip(), cl))
    if len(cl) == 1:
        return {}
    if cl[1] in ARG_CLUBS:
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
    player_pg_link = domitem.find(A, {CLASS: LINK_CLS}, href=True)
    player_pg_url = FUTHEAD_BASE_URL + player_pg_link[HREF]
    player_pg = get(player_pg_url).text
    l = 0
    attempts = 0
    while l <= NATION_IX:
        attempts += 1
        if attempts == 5:
            break
        player_dom = BeautifulSoup(player_pg, HTML_PARSER)
        matching_divs = player_dom.findAll(DIV, {CLASS: NATION_CLS})
        l = len(matching_divs)
    if attempts == 5:
        return {}
    nation = matching_divs[NATION_IX].text.strip()
    for stat in domitem.findAll(SPAN, {CLASS: STAT_CLS}):
        rtg = int(stat.find(SPAN, {CLASS: STAT_VAL_CLS}).text)
        tp = stat.find(SPAN, {CLASS: STAT_TYPE_CLS}).text
        d[tp] = rtg
    ovr = int(domitem.find(SPAN, {CLASS: RATING_CLS}).find(SPAN).text)
    d[NAME] = name
    d[OVR] = ovr
    d[COUNTRY] = nation
    d[POSITION] = pos
    d[LEAGUE] = league
    d[CLUB] = club
    return d


def pull_players(url):
    num_pages = get_list_pages(url)
    pls = []
    for page_num in range(1, num_pages + 1):
        with_page = f'{url}&page={page_num}'
        resp = get(with_page)
        body = BeautifulSoup(resp.text, HTML_PARSER)
        players = body.findAll(DIV, {CLASS: PLAYER_CLS})
        pls += list(map(extract_player_info, players))
    return DataFrame(pls)

def pull_all_players():
    df1 = pull_players(FUTHEAD_NO_PLATFORM_URL)
    df2 = pull_players(GK_URL)
    return concat([df1, df2])

