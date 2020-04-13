from panier import Panier
from oeuf import Oeuf

class Jeu():

    def __init__(self):
        self.panier = Panier()
        self.oeuf = Oeuf()
        self.touches_actives = {}
