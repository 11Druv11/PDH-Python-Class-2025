# pet.py
import random

class Pet:
    def __init__(self, name: str):
        self.name = name

        # Starting stats
        self.hunger = 5      # 0 = full, 10 = starving
        self.happiness = 5   # 0 = sad, 10 = super happy
        self.energy = 5      # 0 = exhausted, 10 = full of energy
        self.toys = 1        # number of toys you can use to cheer them up

        self.game_over = False

    # -------------
    # ACTIONS
    # -------------

    def feed(self):
        self.hunger -= 2
        self.energy += 1

    def play(self):
        # return False if too tired to play
        if self.energy <= 1:
            return False

        self.happiness += 2
        self.hunger += 1
        self.energy -= 2
        return True

    def sleep(self):
        self.energy += 3
        self.hunger += 1

    def use_toy(self):
        if self.toys <= 0:
            return False
        self.toys -= 1
        self.happiness += 3
        return True

    # -------------
    # TURN / EVENTS
    # -------------

    def random_event(self):
        event_roll = random.randint(1, 6)
        msg = None

        if event_roll == 1:
            msg = f"Random Event: {self.name} found a NEW TOY! (+1 toy)"
            self.toys += 1
        elif event_roll == 2:
            msg = f"Random Event: {self.name} learned a trick. (+1 happiness)"
            self.happiness += 1
        elif event_roll == 3:
            msg = f"Random Event: {self.name} snuck a snack. (-1 hunger)"
            self.hunger -= 1
        elif event_roll == 4:
            msg = f"Random Event: Loud noise scared {self.name}. (-1 happiness)"
            self.happiness -= 1
        # 5 and 6 = nothing happens

        return msg

    def decay_over_time(self):
        """Things that happen after each turn, no matter what you do."""
        self.hunger += 1       # gets hungrier over time
        self.happiness -= 1    # gets bored if ignored
        self.energy -= 1       # gets tired just existing :' )

    def clamp_stats(self):
        """Keep values in valid ranges."""
        if self.hunger < 0:
            self.hunger = 0

        if self.happiness > 10:
            self.happiness = 10
        if self.energy > 10:
            self.energy = 10

        if self.happiness < 0:
            self.happiness = 0
        if self.energy < 0:
            self.energy = 0

    def check_game_over_message(self):
        """Return a game over message string, or None if still alive."""
        if self.hunger >= 10:
            return f"{self.name} is STARVING. Game over!"
        if self.happiness <= 0:
            return f"{self.name} is VERY SAD. Game over!"
        if self.energy <= 0:
            return f"{self.name} has no energy left. Game over!"
        return None

    # -------------
    # UTILS
    # -------------

    def status_dict(self):
        """Handy if a UI wants all stats at once."""
        return {
            "hunger": self.hunger,
            "happiness": self.happiness,
            "energy": self.energy,
            "toys": self.toys,
        }
