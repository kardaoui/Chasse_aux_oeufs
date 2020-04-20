import pygame

class Fenetre:

    def __init__(self):
        pygame.init()
        self.hauteur_fenetre = 480
        self.largeur_fenetre = 800
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))

        pygame.display.set_caption("La chasse aux Oeufs")

        self.sol = pygame.image.load("assets/sol.png").convert_alpha()
        self.fond = pygame.image.load("assets/fond.jpg")

        self.fenetre.blit(self.fond, (0, 0))
        self.fenetre.blit(self.sol, (0, 0))

        pygame.display.flip()

    def affichage(self):
        self.fenetre.blit(self.fond, (0, 0))
        self.fenetre.blit(self.sol, (0, 0))


    def afficher_element(self, image, taille):
        self.fenetre.blit(image,taille)
        pygame.display.flip()

if __name__ == '__main__':
    Fenetre()
    rejouer = True
    while rejouer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rejouer = False
                pygame.quit()

