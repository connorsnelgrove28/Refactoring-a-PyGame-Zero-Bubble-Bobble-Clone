import cavern
from .base import ScreenBase

class PlayScreen(ScreenBase):
    def __init__(self, app, Game, Player):
        self.app = app
        self.game = Game(Player())
        cavern.game = self.game
        self.paused = False

    def update(self, input_state):
        if input_state and input_state.pause_pressed:
            self.paused = not self.paused
            return
        if self.paused:
            return
        if self.game.player.lives < 0:
            self.game.play_sound("over")
            from .game_over import GameOverScreen
            self.app.change_screen(GameOverScreen(self.app, self.game))
        else:
            self.game.update(input_state)

    def draw(self):
        self.game.draw()
        cavern.draw_status()
        if self.paused:
            cavern.screen.draw.text("PAUSED", center=(cavern.WIDTH // 2, cavern.HEIGHT // 2), fontsize=64, color="white",)
