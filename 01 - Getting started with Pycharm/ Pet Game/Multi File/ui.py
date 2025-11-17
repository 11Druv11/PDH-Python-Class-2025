# ui.py
import tkinter as tk
from tkinter import simpledialog, messagebox

from pet import Pet


def start_game():
    # -----------------
    # TK ROOT
    # -----------------
    root = tk.Tk()
    root.title("Virtual Pet")

    # Ask for pet name
    name = simpledialog.askstring("Pet Name", "Name your pet:", parent=root)
    if not name:
        name = "Fluffy"

    pet = Pet(name)

    # -----------------
    # UI HELPERS
    # -----------------
    def append_message(msg: str = ""):
        log_text.config(state="normal")
        log_text.insert(tk.END, msg + "\n")
        log_text.see(tk.END)
        log_text.config(state="disabled")

    def update_status_labels():
        hunger_label.config(text=f"Hunger: {pet.hunger} / 10")
        happiness_label.config(text=f"Happiness: {pet.happiness} / 10")
        energy_label.config(text=f"Energy: {pet.energy} / 10")
        toys_label.config(text=f"Toys: {pet.toys}")

    def disable_buttons():
        feed_button.config(state="disabled")
        play_button.config(state="disabled")
        sleep_button.config(state="disabled")
        toy_button.config(state="disabled")

    def show_intro():
        append_message(f"You adopted {pet.name}!")
        append_message(f"Keep {pet.name} fed, happy, and rested.")
        append_message(
            "If hunger reaches 10, or happiness reaches 0, or energy reaches 0, it's game over."
        )
        append_message("")

    # -----------------
    # TURN HANDLING
    # -----------------
    def end_turn():
        if pet.game_over:
            return

        pet.decay_over_time()
        event_msg = pet.random_event()
        pet.clamp_stats()
        update_status_labels()

        if event_msg:
            append_message(event_msg)
            append_message("")

        msg = pet.check_game_over_message()
        if msg is not None:
            pet.game_over = True
            append_message(msg)
            append_message("GAME ENDED")
            disable_buttons()
            messagebox.showinfo("Game Over", msg)

    # -----------------
    # BUTTON CALLBACKS
    # -----------------
    def on_feed_clicked():
        if pet.game_over:
            return
        pet.feed()
        append_message(f"You feed {pet.name} a snack.")
        append_message(f"{pet.name} looks less hungry and a bit more rested.")
        append_message("")
        end_turn()

    def on_play_clicked():
        if pet.game_over:
            return
        if not pet.play():
            append_message(f"{pet.name} is too tired to play right now.")
            append_message("")
            return
        append_message(f"You play with {pet.name}!")
        append_message(f"{pet.name} is happier, but now a little hungry and tired.")
        append_message("")
        end_turn()

    def on_sleep_clicked():
        if pet.game_over:
            return
        pet.sleep()
        append_message(f"{pet.name} takes a nap...")
        append_message(f"{pet.name} feels more rested, but is a bit hungrier.")
        append_message("")
        end_turn()

    def on_toy_clicked():
        if pet.game_over:
            return
        if not pet.use_toy():
            append_message("You have no toys left!")
            append_message("")
            return
        append_message(f"You give {pet.name} a favourite toy!")
        append_message(f"{pet.name} loves it. Happiness goes up!")
        append_message("")
        end_turn()

    def on_quit_clicked():
        root.destroy()

    # -----------------
    # LAYOUT
    # -----------------

    # Title
    title_label = tk.Label(root, text=f"Your pet: {pet.name}", font=("Arial", 16, "bold"))
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

    # Buttons
    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=10)

    feed_button = tk.Button(buttons_frame, text=f"Feed {pet.name}", width=15, command=on_feed_clicked)
    play_button = tk.Button(buttons_frame, text=f"Play with {pet.name}", width=15, command=on_play_clicked)
    sleep_button = tk.Button(buttons_frame, text=f"Let {pet.name} sleep", width=15, command=on_sleep_clicked)
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
