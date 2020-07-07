import sys

import pygame
pygame.init()

from settings import Settings

class Whack:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # Set up the drawing window
        self.screen = pygame.display.set_mode([500, 500])

    # Draw a solid blue circle in the center
    def print_moles(self):
        pygame.draw.circle(self.screen, (150, 150, 255), (250, 250), 20)
        pygame.draw.circle(self.screen, (150, 150, 255), (75, 250), 20)
        pygame.draw.circle(self.screen, (150, 150, 255), (425, 250), 20)
        pygame.draw.circle(self.screen, (150, 150, 255), (250, 75), 20)
        pygame.draw.circle(self.screen, (150, 150, 255), (75, 75), 20)
        pygame.draw.circle(self.screen, (150, 150, 255), (425, 75), 20)
        pygame.draw.circle(self.screen, (150, 150, 255), (250, 425), 20)
        pygame.draw.circle(self.screen, (150, 150, 255), (75, 425), 20)
        pygame.draw.circle(self.screen, (150, 150, 255), (425, 425), 20)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

    def run_game(self):
        while True:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Fill the background with white
            self.screen.fill((255, 255, 255))

            self._update_screen()

            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()

if __name__ == '__main__':
    w = Whack()
    w.run_game()
