import pygame

class Fenetre:

    def __init__(self, panier):
        pygame.init()
        self.panier = panier
        self.hauteur_fenetre = 480
        self.largeur_fenetre = 800
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))

        self.font = pygame.font.SysFont("arial", 25)
        self.score = self.font.render(" Score : {}".format(self.panier.vie), True, pygame.Color("#0A2D5F"))
        self.rect_score = self.score.get_rect()
        #self.rect_score = self.largeur_fenetre / 2

        pygame.display.set_caption("La chasse aux Oeufs")

        self.sol = pygame.image.load("assets/sol.png").convert_alpha()
        self.fond = pygame.image.load("assets/fond.jpg")

    def affichage(self, element):
        self.fenetre.blit(element, (0, 0))

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

