# main.py
# This file contains the GAME LOOP.
# It uses the GameWindow from ui.py and keeps updating it while the game is running.

import time
from ui import GameWindow  # Import our window from the other file


def main():
    # 1. Create the window (from ui.py)
    window = GameWindow()

    # 2. This is our GAME LOOP.
    #    It keeps running while window.running is True.
    while window.running:
        # ---- GAME LOOP STEPS ----
        # 1. Handle input/events
        #    (Tkinter events like button clicks are handled inside window.update())

        # 2. Update game state
        #    Here we could move characters, check collisions, etc.
        #    For this demo, we slowly add 1 point every loop.
        window.score += 1

        # 3. Draw everything
        #    We tell the window to refresh the label and process events.
        window.update()

        # 4. Control the speed of the loop
        #    Sleep a tiny bit so it doesn't run too fast
        time.sleep(0.05)

    print("Game loop has ended. Goodbye!")


if __name__ == "__main__":
    main()
