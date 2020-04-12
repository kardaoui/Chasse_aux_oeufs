import pygame
from jeu import Jeu

jeu = Jeu()


def main():
    pygame.init()

    rejouer = True
    while rejouer:
       # print(jeu.touches_actives)
        hauteur_fenetre, largeur_fenetre = 480, 800
        fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

        pygame.display.set_caption("Lachasse aux Oeufs")

        fond = pygame.image.load("assets/fond.jpg")
        sol = pygame.image.load("assets/sol.png").convert_alpha()

        fenetre.blit(fond, (0, 0))
        fenetre.blit(sol, (0, 0))

        fenetre.blit(jeu.panier.image, (jeu.panier.rect.x, jeu.panier.rect.y))

        """if jeu.touches_actives.get(pygame.K_RIGHT):
            jeu.panier.deplacement(pygame.K_RIGHT)
        elif jeu.touches_actives.get(pygame.K_LEFT):
            jeu.panier.deplacement(pygame.K_LEFT)"""

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rejouer = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                print("ok down")
                jeu.touches_actives[event.key] = True

            if event.type == pygame.KEYUP:
                print("ok up")
                jeu.touches_actives[event.key] = False



if __name__ == '__main__':
    main()
