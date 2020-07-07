import sys
import time

import pygame

from settings import Settings
from mole import Mole

import random

def _seconds_since_epoch():
    return time.mktime(time.localtime())

class Whack:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

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

        self.moles = [self.mole, self.mole2, self.mole3, self.mole4, self.mole5, self.mole6, self.mole7, self.mole8, self.mole9]
        self.timer = 0.0
        self.mole_timer = 0.0
        self.selectedMole = 0
        self.time_since_last_mole = _seconds_since_epoch()
    # Draw a solid blue circle in the center
    def print_moles(self):
        for mole in self.moles:
            mole.blitme()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.print_moles()

        # Flip the display
        pygame.display.flip()

    def _check_mole(self, mouse_pos):
        for mole in self.moles:
            mole_clicked = mole.rect.collidepoint(mouse_pos)
            if mole_clicked:
                mole.clear()
                break

    def _make_mole_alive(self):
        self.selectedMole = random.randint(0, 8)
        self.moles[self.selectedMole].m_time = _seconds_since_epoch()
        print(self.moles[self.selectedMole].m_time)
        self.moles[self.selectedMole].image = pygame.image.load("images/mole.png")

    def _check_events(self):
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mole(mouse_pos)

    def run_game(self):
        self._make_mole_alive()
        while True:
            self._check_events()
            current_time = _seconds_since_epoch()

            #Clear old moles
            for mole in self.moles:
                if current_time - mole.m_time >= 2.0:
                    mole.clear()

            if current_time - self.time_since_last_mole >= 1.0:
                self._make_mole_alive()
                self.time_since_last_mole = current_time
            self._update_screen()
        # Done! Time to quit.
        pygame.quit()

if __name__ == '__main__':
    w = Whack()
    w.run_game()

