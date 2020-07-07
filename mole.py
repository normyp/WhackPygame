import pygame
from pygame.sprite import Sprite

class Mole(Sprite):

    def __init__(self, w_game):
        super().__init__()
        self.alive = True
        self.screen = w_game.screen

        self.image = pygame.image.load("images/mole.png")
        self.rect = self.image.get_rect()

        self._set_active_()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def _set_active_(self):
        self.image.fill((0, 100, 0))


