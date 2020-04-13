import pygame
import random


class Oeuf(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/oeuf.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(70, 730)
        self.rect.y = 0
        self.vitesse = 2

    def chute(self):
        self.rect.y += self.vitesse
