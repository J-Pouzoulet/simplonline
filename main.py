import pandas as pd

from funct_class import*

class Distributeur:
    def __init__(self, name, cane = 100, money = 11.5, cane_price = 1.5):
        self.name = name
        self.cane = cane
        self.money = money
        self.cane_price = cane_price
        self.data_dict = pd.DataFrame({'cane' : [self.cane], 'money' : [self.money]})
        self.data_dict.to_csv('data.csv')
    #def open_csv(self):
     #   open_csv(self)
    #def write_csv(self):
     #   write_csv(self)
    def user_tech(self):
        user_tech(self)
    def buy_cane(self):
        buy_cane(self)
    def load_cane(self):
        load_cane(self)

d1 = Distributeur(name = 'd1')

d1.user_tech()
