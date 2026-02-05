import cavern
from .base import ScreenBase

class PlayScreen(ScreenBase):
    def __init__(self, app, Game, Player):
        self.app = app
        self.game = Game(Player())
        cavern.game = self.game

    def update(self, input_state):
        if self.game.player.lives < 0:
            self.game.play_sound("over")
            from .game_over import GameOverScreen
            self.app.change_screen(GameOverScreen(self.app, self.game))
        else:
            self.game.update(input_state)

    def draw(self):
        self.game.draw()
        cavern.draw_status()
