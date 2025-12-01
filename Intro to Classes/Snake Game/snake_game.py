# snake_game.py
import tkinter as tk
import random

GRID_SIZE = 20   # Number of cells in each direction
CELL = 20        # Pixel size of each cell
SPEED = 120      # ms delay between game loop ticks


class SnakeGame:
    def __init__(self, root):
        self.root = root

        # Create the canvas where we draw the game
        self.canvas = tk.Canvas(
            root,
            width=GRID_SIZE * CELL,
            height=GRID_SIZE * CELL,
            bg="black"
        )
        self.canvas.pack()

        # Bind key events using normal methods (no lambda)
        root.bind("<Up>", self.on_up)
        root.bind("<Down>", self.on_down)
        root.bind("<Left>", self.on_left)
        root.bind("<Right>", self.on_right)

        # Setup game state
        self.reset()

    # ---------- INPUT HANDLERS (these all receive an event) ----------

    def on_up(self, event):
        self.change_direction(0, -1)

    def on_down(self, event):
        self.change_direction(0, 1)

    def on_left(self, event):
        self.change_direction(-1, 0)

    def on_right(self, event):
        self.change_direction(1, 0)

    # ---------- GAME LOGIC ----------

    def reset(self):
        """Reset the entire game to starting conditions."""
        self.direction = (1, 0)  # Start moving right
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.food = self.spawn_food()
        self.game_over = False

    def change_direction(self, dx, dy):
        """Update direction (prevent reversing into ourselves)."""
        old_dx, old_dy = self.direction
        if (dx, dy) != (-old_dx, -old_dy):  # Prevent 180° turn
            self.direction = (dx, dy)

    def spawn_food(self):
        """Place food in a random cell."""
        while True:
            pos = (random.randint(0, GRID_SIZE-1),
                   random.randint(0, GRID_SIZE-1))
            if pos not in self.snake:
                return pos

    def update(self):
        """Advance the game one frame."""
        if self.game_over:
            return

        dx, dy = self.direction
        head_x, head_y = self.snake[0]
        new_head = (head_x + dx, head_y + dy)

        # Check death (wall or self)
        if (
            new_head[0] < 0 or new_head[0] >= GRID_SIZE or
            new_head[1] < 0 or new_head[1] >= GRID_SIZE or
            new_head in self.snake
        ):
            self.game_over = True
            return

        # Move snake
        self.snake.insert(0, new_head)

        # Check food
        if new_head == self.food:
            self.food = self.spawn_food()
        else:
            self.snake.pop()

        # Redraw everything
        self.draw()

    def draw(self):
        """Draw snake and food on the canvas."""
        self.canvas.delete("all")

        # Draw food
        fx, fy = self.food
        self.canvas.create_rectangle(
            fx * CELL, fy * CELL,
            fx * CELL + CELL, fy * CELL + CELL,
            fill="red"
        )

        # Draw snake
        for (x, y) in self.snake:
            self.canvas.create_rectangle(
                x * CELL, y * CELL,
                x * CELL + CELL, y * CELL + CELL,
                fill="lime"
            )
