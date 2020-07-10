class GameStats:

    def __init__(self, w_game):
        self.settings = w_game.settings
        self.reset_stats()
        self.game_active = False
        # High score should never be reset.
        f = open("highscore.txt", "r")
        self.high_score = f.read()
        f.close()

    def clear_high_score(self):
        if not self.high_score:
            self.high_score = 0

    def get_high_score(self):
        return self.high_score

    def reset_stats(self):
        self.lives_left = self.settings.lives_limit
        self.score = 0
        self.level = 1
