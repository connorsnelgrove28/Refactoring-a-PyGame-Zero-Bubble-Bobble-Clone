# Design Overview

## Screen Structure
The game uses an app controller that controls which screen is active. Each screen is responsible for its own update and draw logic. The global update and draw functions only delegate to the App. Screen changes are handled using a single method

## Input Handling
Keyboard input is collected once per frame and is stored in an InputState object. This includes both held keys (left, right, fire held) and edge-detected actions like jumping, firing an orb, starting the game, and pausing the game. The Player class uses InputState instead of reading the keyboard directly.

## Pause
Pause is implemented only in the PlayScreen. Pressing P toggles a paused flag. When paused, the game simulation stops, but the current scene is still drawn with a pause message displayed over top of it. Pressing P then resumes the game again.