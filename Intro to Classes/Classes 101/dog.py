class Dog:
    def __init__(self):
        self.name = ""

    def give_name(self):
        self.name = input(self.name)

    def bark(self):
        print(self.name + " says woof!")
