# ui.py
# This file knows how to build and update the window.
# It does NOT contain the game loop. It just gives us tools for the loop to use.

import tkinter as tk


class GameWindow:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Game Loop Demo")

        # Keep track of whether the window is still open
        self.running = True

        # A simple "score" that we will update in the loop
        self.score = 0

        # Label that shows the score
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 16))
        self.score_label.pack(padx=20, pady=10)

        # Button that lets the player add to the score
        self.add_button = tk.Button(
            self.root,
            text="Click me! (+10 points)",
            font=("Arial", 12),
            command=self.add_points
        )
        self.add_button.pack(padx=20, pady=5)

        # Quit button that tells the loop to stop
        self.quit_button = tk.Button(
            self.root,
            text="Quit",
            font=("Arial", 12),
            command=self.on_quit
        )
        self.quit_button.pack(padx=20, pady=5)

        # If the player clicks the X in the window bar, stop the loop as well
        self.root.protocol("WM_DELETE_WINDOW", self.on_quit)

    def add_points(self):
        """Called when the player presses the 'Click me' button."""
        self.score += 10

    def on_quit(self):
        """Tell the main loop that we want to stop and close the window."""
        self.running = False
        self.root.destroy()

    def update(self):
        """
        Update the text on the screen and process window events.

        This will be called every time through the main game loop.
        """
        # Update the label text
        self.score_label.config(text=f"Score: {self.score}")

        # Let Tkinter handle button clicks, redraws, etc.
        self.root.update_idletasks()
        self.root.update()
