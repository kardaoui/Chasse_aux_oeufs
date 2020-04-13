import pygame
from jeu import Jeu


def main():
    jeu = Jeu()

    hauteur_fenetre, largeur_fenetre = 480, 800
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

    pygame.display.set_caption("La chasse aux Oeufs")

    fond = pygame.image.load("assets/fond.jpg")
    sol = pygame.image.load("assets/sol.png").convert_alpha()

    rejouer = True
    while rejouer:
        fenetre.blit(fond, (0, 0))
        fenetre.blit(sol, (0, 0))

        fenetre.blit(jeu.oeuf.image, (jeu.oeuf.rect.x, jeu.oeuf.rect.y))

        fenetre.blit(jeu.panier.image, (jeu.panier.rect.x, jeu.panier.rect.y))

        jeu.oeuf.chute()

        pygame.display.flip()

        if jeu.touches_actives.get(pygame.K_RIGHT) and jeu.panier.rect.x + jeu.panier.rect.width < largeur_fenetre:
            jeu.panier.deplacement(pygame.K_RIGHT)
        elif jeu.touches_actives.get(pygame.K_LEFT) and jeu.panier.rect.x > 0:
            jeu.panier.deplacement(pygame.K_LEFT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rejouer = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                jeu.touches_actives[event.key] = True

            if event.type == pygame.KEYUP:
                jeu.touches_actives[event.key] = False


if __name__ == '__main__':
    pygame.init()
    main()
