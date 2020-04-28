import pygame

from fenetre import Fenetre
from panier import Panier
from oeuf import Oeuf


class Jeu:

    def __init__(self):

        self.panier = Panier()
        self.fenetre = Fenetre(self.panier)
        self.oeuf = Oeuf(self.panier)
        self.rejouer = True
        self.compteur = 0

        self.touches_actives = {}
        self.timer = pygame.time.Clock()
        self.group_oeufs = pygame.sprite.Group()

    def verifier_collision(self, oeuf, panier):
        if pygame.sprite.spritecollide(oeuf, panier, True) and oeuf:
            self.panier.vie += 2
            print(self.panier.vie)

    def jouer(self):
        while self.rejouer:

            self.fenetre.affichage(self.fenetre.fond)

            if self.compteur == 0:
                self.compteur = 80
                self.oeuf.groupe_oeuf.add(Oeuf(self.panier))

            self.oeuf.chute(self.oeuf.groupe_oeuf)

            self.fenetre.dessiner_groupe(self.oeuf.groupe_oeuf)

            self.fenetre.affichage(self.fenetre.sol)

            self.fenetre.dessiner_groupe(self.panier.groupe_panier)

            self.verifier_collision(self.panier, self.oeuf.groupe_oeuf)

            self.fenetre.affichage(self.fenetre.score)

            self.fenetre.rafraichir_fenetre()

            if self.touches_actives.get(pygame.K_RIGHT) and \
                    self.panier.rect.x + self.panier.rect.width < self.fenetre.largeur_fenetre:
                self.panier.deplacement(pygame.K_RIGHT)
            elif self.touches_actives.get(pygame.K_LEFT) and \
                    self.panier.rect.x > 0:
                self.panier.deplacement(pygame.K_LEFT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rejouer = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    self.touches_actives[event.key] = True
                if event.type == pygame.KEYUP:
                    self.touches_actives[event.key] = False

            self.timer.tick(60)
            self.compteur -= 1


if __name__ == '__main__':
    Jeu()
    Jeu().jouer()
