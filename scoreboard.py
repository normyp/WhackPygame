import pygame.font
from pygame.sprite import Group

class Scoreboard:

    def __init__(self, w_game):
        self.w_game = w_game
        self.screen = w_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = w_game.stats
        self.settings = w_game.settings

        self.text_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_colour, self.settings.bg_color)
        #Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw scores, level and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
