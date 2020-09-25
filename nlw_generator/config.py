from bs4 import BeautifulSoup
from requests import get

# URL details
PLATFORM = 'xb'
FUTHEAD_URL = f'https://www.futhead.com/21/players/?bin_platform={PLATFORM}'
FUTHEAD_NO_PLATFORM_URL = 'https://www.futhead.com/21/players/?page='

# Parsing constants
HTML_PARSER = 'html.parser'
SPAN = 'span'
DIV = 'div'
CLASS = 'class'
STRONG = 'strong'
PGS_CLS = 'font-12 font-bold margin-l-r-10'
PLAYER_CLS = 'content player-item font-24'
PLAYER_NAME = 'player-name'
CLUB_LEAGUE_INFO = 'player-club-league-name'

# Buggy constants to account for
ARG = 'Argentina'
BETTER_ARG = 'Argentina Primera División'
SERIE_B = 'Italy Serie B'
CHILE = 'Chile Campeonato Nacional Scotiabank'
BUGGY_ARGENTINA_CLUBS = ['River Plate', 'Boca Juniors', 'Racing Club de Avellaneda', 'Lanús', 'Vélez Sarsfield']
SERIE_B_CLUBS = ['Brescia']
CHILE_CLUBS = ['Universidad Católica']

# Dataframe columns
NAME = 'name'
POSITION = 'pos'
LEAGUE = 'league'
CLUB = 'club'

