import pygame

class Mole:

    def __init__(self, w_game):
        self.alive = True
        self.screen = w_game.screen
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("mole.png")

    def blitme(self):
        self.screen.blit(self.image, self.rect)


