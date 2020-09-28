from nlw_generator.config.dataframe_cols import LEAGUE, CLUB, \
                                                COUNTRY, NAME
from nlw_generator.config.formation import POS, LINKS, ACTIVE_P

class Formation:

    def __init__(self, fpath):
        self.slots = []
        with open(fpath, 'r') as f:
            for line in f.readlines():
                s = line.split(' ')
                d = {}
                d[POS] = s[0]
                d[LINKS] = [int(l) for l in s[1:]]
                d[ACTIVE_P] = None
                self.slots.append(d)
        self.active_players = 0

    def insert(self, ix, player):
        self.active_players += 1
        self.slots[ix][ACTIVE_P] = player

    def is_nlw(self):
        for slot in self.slots:
            links_counted = 0
            player = slot[ACTIVE_P]
            if player is not None:
                green_links = 0
                red_links = 0
                for link in slot[LINKS]:
                    link_p = self.slots[link][ACTIVE_P]
                    if link_p is None:
                        break
                    else:
                        links_counted += 1
                        if player[LEAGUE] == link_p[LEAGUE]:
                            if player[CLUB] == link_p[CLUB]:
                                if player[COUNTRY] == link_p[COUNTRY]:
                                    green_links += 2
                                else:
                                    green_links += 1
                            elif player[COUNTRY] == link_p[COUNTRY]:
                                green_links += 1
                            else:
                                red_links += .5
                                green_links += .5
                        elif player[COUNTRY] == link_p[COUNTRY]:
                            red_links += .5
                            green_links += .5
                        else:
                            red_links += 1
            if links_counted == len(slot[LINKS]):
                if green_links != red_links:
                    return False
        return True

