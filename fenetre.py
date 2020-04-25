import pygame

class Fenetre:

    def __init__(self):
        pygame.init()
        self.pyGame = pygame
        self.hauteur_fenetre = 480
        self.largeur_fenetre = 800
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))

        pygame.display.set_caption("La chasse aux Oeufs")

        self.sol = pygame.image.load("assets/sol.png").convert_alpha()
        self.fond = pygame.image.load("assets/fond.jpg")

    def affichage_fond(self):
        self.fenetre.blit(self.fond, (0, 0))

    def affichage_sol(self):
        self.fenetre.blit(self.sol, (0, 0))

    def dessiner_groupe(self, group):
        group.draw(self.fenetre)

    def rafraichir_fenetre(self):
        pygame.display.flip()

if __name__ == '__main__':
    Fenetre()
    rejouer = True
    while rejouer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rejouer = False
                pygame.quit()

