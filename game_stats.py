class GameStats:

    def __init__(self, w_game):
        self.settings = w_game.settings
        self.reset_stats()
        self.game_active = False
        # High score should never be reset.
        f = open("highscore.txt", "r")
        self.high_score = f.read()
        f.close()
        self.old_high_score = self.high_score

    def reset_stats(self):
        self.lives_left = self.settings.lives_limit
        self.score = 0
        self.level = 1

    def set_old_high_score(self):
        f = open("highscore.txt", "r")
        self.old_high_score = int(f.read())
        f.close()
        if int(self.get_high_score()) > int(self.old_high_score):
            f = open("highscore.txt", "w")
            self.old_high_score = self.get_high_score()
            f.write(str(self.old_high_score))
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

    def increment_game_score(self, points):
        self.score += points

    def decrement_game_score(self, points):
        self.score -= points
