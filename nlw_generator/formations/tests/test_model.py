from nlw_generator.formations.model import Formation
from nlw_generator.config.dataframe_cols import NAME
from unittest import TestCase
from pandas import read_csv

def by_name(df, name):
    return df[df[NAME] == name].iloc[0]


class Test_IsNLW_Valid(TestCase):

    def setUp(self):
        self.players = read_csv('players.csv')
        self.formation = Formation('4332.form')
    
    def test_valid_nlw(self):
        self.formation.insert(0, by_name(self.players, \
                                         'Alphonse Areola'))
        self.formation.insert(1, by_name(self.players, \
                                         'Theo Hernández'))
        self.formation.insert(2, by_name(self.players, \
                                         'Lucas Hernández'))
        self.formation.insert(3, by_name(self.players, \
                                         'Dayot Upamecano'))
        self.formation.insert(4, by_name(self.players, \
                                         'Kévin Malcuit'))
        self.formation.insert(5, by_name(self.players, \
                                         'Arturo Vidal'))
        self.formation.insert(6, by_name(self.players, \
                                         'Marcelo Brozović'))
        self.formation.insert(7, by_name(self.players, \
                                         'Radja Nainggolan'))
        self.formation.insert(8, by_name(self.players, \
                                         'Yannick Carrasco'))
        self.formation.insert(9, by_name(self.players, \
                                         'João Félix'))
        self.formation.insert(10, by_name(self.players, \
                                          'Ángel Correa'))
        self.assertTrue(self.formation.is_nlw())

class Test_IsNLW_Invalid(TestCase):

    def setup(self):
        self.players = read_csv('players.csv')
        self.formation = Formation('4332.form')
    
    def test_invalid_nlw(self):
        pass
