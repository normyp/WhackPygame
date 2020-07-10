import pygame.font
from pygame.sprite import Group

class Scoreboard:

    def __init__(self, w_game):
        self.w_game = w_game
        self.screen = w_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = w_game.stats
        self.settings = w_game.settings

        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_colour, None)
        #Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = self.stats.high_score
        high_score_str = "High Score: {:}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_colour, None)
        #Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 20
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw scores, level and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self):
        """Check to see if there's a new high score."""
        self.stats.clear_high_score()
        if self.stats.score > int(self.stats.high_score):
            self.stats.high_score = self.stats.score
            self.prep_high_score()
