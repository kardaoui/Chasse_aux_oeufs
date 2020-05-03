import pygame

class Fenetre:

    def __init__(self):
        pygame.init()
        self.hauteur_fenetre = 480
        self.largeur_fenetre = 800
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))

        self.font = pygame.font.SysFont("arial", 25)

        pygame.display.set_caption("La chasse aux Oeufs")

        self.sol = pygame.image.load("assets/sol.png").convert_alpha()
        self.fond = pygame.image.load("assets/fond.jpg")

    def affichage(self, element):
        self.fenetre.blit(element, (0, 0))

    def dessiner_groupe(self, group):
        group.draw(self.fenetre)

    def rafraichir_fenetre(self):
        pygame.display.flip()

    def afficher_score(self, p):
        self.score = self.font.render(" Score : {}".format(p), True, pygame.Color("#0A2D5F"))


if __name__ == '__main__':
    Fenetre()
    rejouer = True
    while rejouer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rejouer = False
                pygame.quit()

