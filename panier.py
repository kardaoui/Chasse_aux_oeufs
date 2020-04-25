import pygame


class Panier(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/panier.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300
        self.vitesse = 5

        self.event_key_droite = pygame.K_RIGHT
        self.event_key_gauche = pygame.K_LEFT

        self.groupe_panier = pygame.sprite.Group()
        self.groupe_panier.add(self)

    def deplacement(self, direction):
        if direction == self.event_key_droite:
            self.rect.x += self.vitesse
        if direction == self.event_key_gauche:
            self.rect.x -= self.vitesse


