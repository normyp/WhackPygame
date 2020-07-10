import pygame
import time
from pygame.sprite import Sprite

class Mole(Sprite):

    def __init__(self, w_game):
        super().__init__()
        self.m_time = 0
        self.screen = w_game.screen

        self.image = pygame.image.load("images/mole.png")
        self.rect = self.image.get_rect()

        self.clear()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def is_alive(self):
        return self.m_time != 0

    def clear(self):
        self.image.fill((0, 0, 0, 0))
        self.m_time = 0


