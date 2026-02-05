class App:
    def __init__(self, start_screen):
        self.screen = start_screen

    def change_screen(self, new_screen):
        self.screen = new_screen

    def update(self, input_state):
        self.screen.update(input_state)

    def draw(self):
        self.screen.draw()
