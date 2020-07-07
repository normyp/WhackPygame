import sys

import pygame
pygame.init()

from settings import Settings
from mole import Mole

class Whack:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode([500, 500])

        self.mole = Mole(self)
        self.mole2 = Mole(self)
        self.mole3 = Mole(self)
        self.mole4 = Mole(self)
        self.mole5 = Mole(self)
        self.mole6 = Mole(self)
        self.mole7 = Mole(self)
        self.mole8 = Mole(self)
        self.mole9 = Mole(self)
        self.mole.rect.x += 25
        self.mole.rect.y += 0

        self.mole2.rect.x += 200
        self.mole2.rect.y += 0

        self.mole3.rect.x += 375
        self.mole3.rect.y += 0

        self.mole4.rect.x += 25
        self.mole4.rect.y += 175

        self.mole5.rect.x += 200
        self.mole5.rect.y += 175

        self.mole6.rect.x += 375
        self.mole6.rect.y += 175

        self.mole7.rect.x += 25
        self.mole7.rect.y += 350

        self.mole8.rect.x += 200
        self.mole8.rect.y += 350

        self.mole9.rect.x += 375
        self.mole9.rect.y += 350
    # Draw a solid blue circle in the center
    def print_moles(self):
        self.mole.blitme()
        self.mole2.blitme()
        self.mole3.blitme()
        self.mole4.blitme()
        self.mole5.blitme()
        self.mole6.blitme()
        self.mole7.blitme()
        self.mole8.blitme()
        self.mole9.blitme()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.print_moles()

        # Flip the display
        pygame.display.flip()


    def _check_events(self):
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    #def _change_mole_pos(self):

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            #self._change_mole_pos()
        # Done! Time to quit.
        pygame.quit()

if __name__ == '__main__':
    w = Whack()
    w.run_game()
