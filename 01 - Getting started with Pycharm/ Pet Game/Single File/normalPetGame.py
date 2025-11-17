import random

# -----------------
# SETUP / START
# -----------------

# Ask the player to name the pet
name = input("Name your pet: ")

# Starting stats
hunger = 5        # 0 = full, 10 = starving
happiness = 5     # 0 = sad, 10 = super happy
energy = 5        # 0 = exhausted, 10 = full of energy
toys = 1          # number of toys you can use to cheer them up

print("")
print("You adopted " + name + "!")
print("Keep " + name + " fed, happy, and rested.")
print("If hunger gets to 10, or happiness gets to 0, or energy gets to 0, it's game over.")
print("")


# -----------------
# FUNCTIONS
# -----------------

def show_status():
    print("----- STATUS -----")
    print(name + "'s hunger: " + str(hunger) + " / 10")
    print(name + "'s happiness: " + str(happiness) + " / 10")
    print(name + "'s energy: " + str(energy) + " / 10")
    print("Toys: " + str(toys))
    print("------------------")
    print("")


def feed_pet():
    # we need to say we are using the outer variables
    global hunger, energy
    print("You feed " + name + " a snack.")
    hunger = hunger - 2
    energy = energy + 1
    print(name + " looks less hungry and a bit more rested.")
    print("")


def play_with_pet():
    global happiness, hunger, energy
    if energy <= 1:
        print(name + " is too tired to play right now.")
        print("")
        return

    print("You play with " + name + "!")
    happiness = happiness + 2
    hunger = hunger + 1
    energy = energy - 2
    print(name + " is happier, but now a little hungry and tired.")
    print("")


def let_pet_sleep():
    global energy, hunger
    print(name + " takes a nap...")
    energy = energy + 3
    hunger = hunger + 1
    print(name + " feels more rested, but is a bit hungrier.")
    print("")


def use_toy():
    global toys, happiness
    if toys > 0:
        print("You give " + name + " a favourite toy!")
        toys = toys - 1
        happiness = happiness + 3
        print(name + " loves it. Happiness goes up!")
        print("")
    else:
        print("You have no toys left!")
        print("")


def random_event():
    # random surprise at the end of each turn
    global toys, happiness, hunger, energy
    event_roll = random.randint(1, 6)

    if event_roll == 1:
        print("Random Event: " + name + " found a NEW TOY! (+1 toy)")
        toys = toys + 1
    elif event_roll == 2:
        print("Random Event: " + name + " learned a trick. (+1 happiness)")
        happiness = happiness + 1
    elif event_roll == 3:
        print("Random Event: " + name + " snuck a snack. (-1 hunger)")
        hunger = hunger - 1
    elif event_roll == 4:
        print("Random Event: Loud noise scared " + name + ". (-1 happiness)")
        happiness = happiness - 1
    # 5 and 6 = nothing happens
    print("")


def clamp_stats():
    # make sure values stay in range
    global hunger, happiness, energy
    if hunger < 0:
        hunger = 0
    if happiness > 10:
        happiness = 10
    if energy > 10:
        energy = 10
    # we do NOT clamp upper hunger because 10 is danger
    # but we'll stop it going lower than 0
    if happiness < 0:
        happiness = 0
    if energy < 0:
        energy = 0


def decay_over_time():
    # every turn, time passes
    global hunger, happiness, energy
    hunger = hunger + 1         # gets hungrier over time
    happiness = happiness - 1   # gets bored if ignored
    energy = energy - 1         # gets tired just existing :')

def check_game_over():
    if hunger >= 10:
        print(name + " is STARVING. Game over!")
        return True
    if happiness <= 0:
        print(name + " is VERY SAD. Game over!")
        return True
    if energy <= 0:
        print(name + " has no energy left. Game over!")
        return True
    return False


# -----------------
# MAIN GAME LOOP
# -----------------

while True:
    show_status()

    print("What do you want to do?")
    print("1. Feed " + name)
    print("2. Play with " + name)
    print("3. Let " + name + " sleep")
    print("4. Use a toy")
    print("5. Quit")
    choice = input("> ")

    if choice == "1":
        feed_pet()
    elif choice == "2":
        play_with_pet()
    elif choice == "3":
        let_pet_sleep()
    elif choice == "4":
        use_toy()
    elif choice == "5":
        print("You say goodbye to " + name + ". Thanks for playing!")
        break
    else:
        print("Please choose 1, 2, 3, 4 or 5.")
        print("")
        continue

    # time passes after the action
    decay_over_time()

    # something random might happen
    random_event()

    # keep stats sane
    clamp_stats()

    # check if we lost
    if check_game_over():
        break

print("GAME ENDED")