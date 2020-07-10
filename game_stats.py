class GameStats:

    def __init__(self, w_game):
        self.settings = w_game.settings
        self.reset_stats()
        self.game_active = False
        # High score should never be reset.
        f = open("highscore.txt", "r")
        self.high_score = f.read()
        f.close()

    def get_high_score(self):
        return self.high_score

    def new_high_score_set(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            return True
        return False

    def get_rounded_score(self):
        return round(self.score, -1)

    def reset_stats(self):
        self.lives_left = self.settings.lives_limit
        self.score = 0
        self.level = 1
