import pygame

from fenetre import Fenetre
from panier import Panier
from oeuf import Oeuf

class Jeu:

    def __init__(self):
        self.fenetre = Fenetre()
        self.panier = Panier()
        self.oeuf = Oeuf()

        self.rejouer = True
        self.compteur = 0

        self.touches_actives = {}
        self.timer = pygame.time.Clock()

        self.ajouter_a_groupe(self.panier , self.panier.groupe_panier)

    def ajouter_a_groupe(self, element,group):
        group.add(element)

    def jouer(self):
        while self.rejouer:

            self.fenetre.affichage_arriere_plan()

            for oeuf in self.oeuf.group_oeufs:
                oeuf.chute()

            if self.compteur == 0:
                self.newoeuf = Oeuf()
                self.ajouter_a_groupe(self.newoeuf, self.oeuf.group_oeufs)
                self.compteur = 300
                print(len(self.oeuf.group_oeufs))


            self.fenetre.dessiner_groupe(self.oeuf.group_oeufs)
            self.fenetre.dessiner_groupe(self.panier.groupe_panier)

            self.fenetre.rafraichir_fenetre()

            if self.touches_actives.get(pygame.K_RIGHT) and self.panier.rect.x + self.panier.rect.width < self.fenetre.largeur_fenetre:
                self.panier.deplacement(pygame.K_RIGHT)
            elif self.touches_actives.get(pygame.K_LEFT) and self.panier.rect.x > 0:
                self.panier.deplacement(pygame.K_LEFT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rejouer = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    self.touches_actives[event.key] = True
                if event.type == pygame.KEYUP:
                    self.touches_actives[event.key] = False


            self.timer.tick(250)
            self.compteur -= 1

if __name__ == '__main__':
    Jeu()
    Jeu().jouer()


