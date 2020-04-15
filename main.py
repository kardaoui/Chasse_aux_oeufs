import pygame
from jeu import Jeu


def main():
    jeu = Jeu()

    delai = 20
    timer = pygame.time.Clock()
    hauteur_fenetre, largeur_fenetre = 480, 800
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

    pygame.display.set_caption("La chasse aux Oeufs")

    sol = pygame.image.load("assets/sol.png").convert_alpha()
    fond = pygame.image.load("assets/fond.jpg")

    oeufs = pygame.sprite.Group()

    pygame.display.flip()

    rejouer = True
    while rejouer:

        if delai > 0:
            delai-=1
            print(delai)
        else:
            new_oeuf = Jeu().oeuf
            oeufs.add(new_oeuf)
            delai = 70

        fenetre.blit(fond, (0, 0))
        fenetre.blit(sol, (0, 0))

        for oeuf in oeufs:
            oeuf.chute()

        # fenetre.blit(jeu.oeuf.image, (jeu.oeuf.rect.x, jeu.oeuf.rect.y))

        oeufs.draw(fenetre)

        fenetre.blit(jeu.panier.image, (jeu.panier.rect.x, jeu.panier.rect.y))

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

        timer.tick(100)

if __name__ == '__main__':
    pygame.init()
    main()
