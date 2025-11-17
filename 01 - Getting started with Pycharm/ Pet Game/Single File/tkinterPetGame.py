import random
import tkinter as tk
from tkinter import simpledialog, messagebox

# -----------------
# SETUP / START
# -----------------

# Starting stats
hunger = 5        # 0 = full, 10 = starving
happiness = 5     # 0 = sad, 10 = super happy
energy = 5        # 0 = exhausted, 10 = full of energy
toys = 1          # number of toys you can use to cheer them up
game_over = False

name = "Pet"  # will be set via dialog later

# -----------------
# UI HELPERS
# -----------------

def append_message(msg: str):
    """Add text to the log area."""
    log_text.config(state="normal")
    log_text.insert(tk.END, msg + "\n")
    log_text.see(tk.END)
    log_text.config(state="disabled")


def update_status_labels():
    """Refresh the labels to show current stats."""
    hunger_label.config(text=f"Hunger: {hunger} / 10")
    happiness_label.config(text=f"Happiness: {happiness} / 10")
    energy_label.config(text=f"Energy: {energy} / 10")
    toys_label.config(text=f"Toys: {toys}")


def disable_buttons():
    feed_button.config(state="disabled")
    play_button.config(state="disabled")
    sleep_button.config(state="disabled")
    toy_button.config(state="disabled")


# -----------------
# GAME LOGIC
# -----------------

def show_intro():
    append_message(f"You adopted {name}!")
    append_message(f"Keep {name} fed, happy, and rested.")
    append_message(
        "If hunger reaches 10, or happiness reaches 0, or energy reaches 0, it's game over."
    )
    append_message("")


def feed_pet():
    global hunger, energy
    append_message(f"You feed {name} a snack.")
    hunger = hunger - 2
    energy = energy + 1
    append_message(f"{name} looks less hungry and a bit more rested.")
    append_message("")


def play_with_pet():
    global happiness, hunger, energy
    if energy <= 1:
        append_message(f"{name} is too tired to play right now.")
        append_message("")
        return

    append_message(f"You play with {name}!")
    happiness = happiness + 2
    hunger = hunger + 1
    energy = energy - 2
    append_message(f"{name} is happier, but now a little hungry and tired.")
    append_message("")


def let_pet_sleep():
    global energy, hunger
    append_message(f"{name} takes a nap...")
    energy = energy + 3
    hunger = hunger + 1
    append_message(f"{name} feels more rested, but is a bit hungrier.")
    append_message("")


def use_toy():
    global toys, happiness
    if toys > 0:
        append_message(f"You give {name} a favourite toy!")
        toys = toys - 1
        happiness = happiness + 3
        append_message(f"{name} loves it. Happiness goes up!")
        append_message("")
    else:
        append_message("You have no toys left!")
        append_message("")


def random_event():
    global toys, happiness, hunger, energy
    event_roll = random.randint(1, 6)

    if event_roll == 1:
        append_message(f"Random Event: {name} found a NEW TOY! (+1 toy)")
        toys = toys + 1
    elif event_roll == 2:
        append_message(f"Random Event: {name} learned a trick. (+1 happiness)")
        happiness = happiness + 1
    elif event_roll == 3:
        append_message(f"Random Event: {name} snuck a snack. (-1 hunger)")
        hunger = hunger - 1
    elif event_roll == 4:
        append_message(f"Random Event: Loud noise scared {name}. (-1 happiness)")
        happiness = happiness - 1
    # 5 and 6 = nothing happens
    append_message("")


def clamp_stats():
    global hunger, happiness, energy
    if hunger < 0:
        hunger = 0
    if happiness > 10:
        happiness = 10
    if energy > 10:
        energy = 10
    if happiness < 0:
        happiness = 0
    if energy < 0:
        energy = 0


def decay_over_time():
    global hunger, happiness, energy
    hunger = hunger + 1         # gets hungrier over time
    happiness = happiness - 1   # gets bored if ignored
    energy = energy - 1         # gets tired just existing


def check_game_over_message():
    """Return a game over message, or None if still alive."""
    if hunger >= 10:
        return f"{name} is STARVING. Game over!"
    if happiness <= 0:
        return f"{name} is VERY SAD. Game over!"
    if energy <= 0:
        return f"{name} has no energy left. Game over!"
    return None


def end_turn():
    """Things that happen after each action."""
    global game_over

    if game_over:
        return

    decay_over_time()
    random_event()
    clamp_stats()
    update_status_labels()

    msg = check_game_over_message()
    if msg is not None:
        game_over = True
        append_message(msg)
        append_message("GAME ENDED")
        disable_buttons()
        messagebox.showinfo("Game Over", msg)


# -----------------
# BUTTON CALLBACKS
# -----------------

def on_feed_clicked():
    if game_over:
        return
    feed_pet()
    end_turn()


def on_play_clicked():
    if game_over:
        return
    play_with_pet()
    end_turn()


def on_sleep_clicked():
    if game_over:
        return
    let_pet_sleep()
    end_turn()


def on_toy_clicked():
    if game_over:
        return
    use_toy()
    end_turn()


def on_quit_clicked():
    root.destroy()


# -----------------
# TKINTER UI SETUP
# -----------------

root = tk.Tk()
root.title("Virtual Pet")

# Ask for pet name
name = simpledialog.askstring("Pet Name", "Name your pet:", parent=root)
if not name:
    name = "Fluffy"

# Top: Pet name
title_label = tk.Label(root, text=f"Your pet: {name}", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Status frame
status_frame = tk.Frame(root)
status_frame.pack(pady=5)

hunger_label = tk.Label(status_frame, text="Hunger: ?", width=20, anchor="w")
happiness_label = tk.Label(status_frame, text="Happiness: ?", width=20, anchor="w")
energy_label = tk.Label(status_frame, text="Energy: ?", width=20, anchor="w")
toys_label = tk.Label(status_frame, text="Toys: ?", width=20, anchor="w")

hunger_label.grid(row=0, column=0, padx=5, pady=2, sticky="w")
happiness_label.grid(row=1, column=0, padx=5, pady=2, sticky="w")
energy_label.grid(row=0, column=1, padx=5, pady=2, sticky="w")
toys_label.grid(row=1, column=1, padx=5, pady=2, sticky="w")

# Buttons frame
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

feed_button = tk.Button(buttons_frame, text=f"Feed {name}", width=15, command=on_feed_clicked)
play_button = tk.Button(buttons_frame, text=f"Play with {name}", width=15, command=on_play_clicked)
sleep_button = tk.Button(buttons_frame, text=f"Let {name} sleep", width=15, command=on_sleep_clicked)
toy_button = tk.Button(buttons_frame, text="Use a toy", width=15, command=on_toy_clicked)
quit_button = tk.Button(buttons_frame, text="Quit", width=15, command=on_quit_clicked)

feed_button.grid(row=0, column=0, padx=5, pady=5)
play_button.grid(row=0, column=1, padx=5, pady=5)
sleep_button.grid(row=1, column=0, padx=5, pady=5)
toy_button.grid(row=1, column=1, padx=5, pady=5)
quit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Log / messages
log_text = tk.Text(root, width=60, height=15, state="disabled")
log_text.pack(padx=10, pady=10)

# Initial status + intro
update_status_labels()
show_intro()

root.mainloop()
