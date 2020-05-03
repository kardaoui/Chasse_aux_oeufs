import pygame
import random


class Oeuf(pygame.sprite.Sprite):

    def __init__(self, panier):
        super().__init__()
        self.panier = panier
        self.image = pygame.image.load("assets/oeuf.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(70, 730)
        self.rect.y = 0
        self.vitesse = random.randint(2, 5)
        # self.vitesse = 2

        self.groupe_oeuf = pygame.sprite.Group()

    def chute(self, group , panier):
        for oeuf_ in group:
            if oeuf_.rect.y < 410:
                oeuf_.rect.y += oeuf_.vitesse

                if pygame.sprite.spritecollide(oeuf_, panier.groupe_panier, False) \
                        and oeuf_.rect.top > 350 \
                        and self.panier.rect.left <= oeuf_.rect.centerx <= self.panier.rect.right:
                    self.panier.vie += 2
                    group.remove(oeuf_)
            else:
                group.remove(oeuf_)
                self.panier.vie -= 2

