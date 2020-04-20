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
        self.touches_actives = {}
        self.timer = pygame.time.Clock()

    def jouer(self):
        while self.rejouer:

            self.fenetre.affichage()

            self.fenetre.afficher_element(self.panier.image, (self.panier.rect.x, self.panier.rect.y))
            self.fenetre.afficher_element(self.oeuf.image, (self.oeuf.rect.x, self.oeuf.rect.y))

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
        self.timer.tick(30)

if __name__ == '__main__':
    Jeu()
    Jeu().jouer()


