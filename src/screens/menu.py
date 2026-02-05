import cavern
from .base import ScreenBase

class MenuScreen(ScreenBase):
    def __init__(self, app, Game):
        self.app = app
        self.game = Game()
        cavern.game = self.game

    def update(self, input_state):
        if input_state and input_state.fire_pressed:
            from .play import PlayScreen
            self.app.change_screen(PlayScreen(self.app, cavern.Game, cavern.Player))
        else:
            self.game.update()


    def draw(self):
        self.game.draw()
        cavern.screen.blit("title", (0, 0))
        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        cavern.screen.blit("space" + str(anim_frame), (130, 280))
