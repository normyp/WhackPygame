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

        self.moles = [Mole(self) for i in range(9)]
        x_values = [25, 200, 375]
        y_values = [0, 175, 350]
        for i in range(0, 9):
            mole = Mole(self)
            mole.rect.x = x_values[i % 3]
            mole.rect.y = y_values[i // 3]
            self.moles[i] = mole

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
        #Randomly picks a mole to spawn
        self.selectedMole = random.randint(0, 8)
        #Time since spawn
        self.moles[self.selectedMole].m_time = _seconds_since_epoch()
        if self.moles[self.selectedMole].is_alive:
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
            
            # Clear old moles
            for mole in self.moles:
                random_time = random.randint(3, 6)
                print("Random time is ", random_time)
                if current_time - mole.m_time >= random_time:
                    mole.clear()

            # Spawn a mole every second
            if current_time - self.time_since_last_mole >= 1.0:
                self._make_mole_alive()
                self.time_since_last_mole = current_time

            self._update_screen()
        # Done! Time to quit.
        pygame.quit()

if __name__ == '__main__':
    w = Whack()
    w.run_game()

