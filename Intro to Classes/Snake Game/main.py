# main.py
from snake_game import SnakeGame
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Snake Game – Press R to Restart")

    game = SnakeGame(root)

    # Bind restart key using a normal function
    def on_restart(event):
        game.reset()

    root.bind("r", on_restart)
    root.bind("R", on_restart)  # allow uppercase R too

    # GAME LOOP
    def loop():
        game.update()
        root.after(120, loop)

    loop()
    root.mainloop()


if __name__ == "__main__": # The __name__ variable is a secret variable python gives to every file. If this is the file that we are running (not importing), than this __name__ variable will be called __main__
    main()
