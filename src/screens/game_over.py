import cavern
from .base import ScreenBase

class GameOverScreen(ScreenBase):
    def __init__(self, app, game):
        self.app = app
        self.game = game
        cavern.game = self.game

    def update(self, input_state):
        if input_state and input_state.fire_pressed:
            from .menu import MenuScreen
            self.app.change_screen(MenuScreen(self.app, cavern.Game))


    def draw(self):
        self.game.draw()
        cavern.draw_status()
        cavern.screen.blit("over", (0, 0))
