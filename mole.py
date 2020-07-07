import pygame
from pygame.sprite import Sprite

class Mole(Sprite):

    def __init__(self, w_game):
        self.alive = True
        self.screen = w_game.screen

        self.image = pygame.image.load("images/mole.png")
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)


