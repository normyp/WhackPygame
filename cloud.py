import pygame
from pygame.sprite import Sprite

class Cloud(Sprite):

    def __init__(self, w_game):
        super().__init__()

        self.screen = w_game.screen
        self.w_game = w_game
        self.original_image = pygame.image.load("images/cloud.png")
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def make_alpha(self):
        self.image.fill((255, 255, 255, 0), None, pygame.BLEND_RGBA_MULT)

