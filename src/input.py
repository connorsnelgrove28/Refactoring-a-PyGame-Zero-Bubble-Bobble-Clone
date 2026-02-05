from dataclasses import dataclass

@dataclass(frozen=True)
class InputState:
    left: bool
    right: bool
    jump_pressed: bool
    fire_pressed: bool
    fire_held: bool
    pause_pressed: bool


class InputTracker:
    def __init__(self):
        self._prev_space = False
        self._prev_up = False
        self._prev_p = False

    def build(self, keyboard) -> InputState:
        space_now = keyboard.space
        up_now = keyboard.up
        p_now = keyboard.p

        return InputState(
            left=keyboard.left,
            right=keyboard.right,
            jump_pressed=up_now and not self._prev_up,
            fire_pressed=space_now and not self._prev_space,
            fire_held=space_now,
            pause_pressed=p_now and not self._prev_p,
        )

    def advance(self, keyboard):
        self._prev_space = keyboard.space
        self._prev_up = keyboard.up
        self._prev_p = keyboard.p
