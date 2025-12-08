class Dog_Class:
    def __init__(self):
        self.name = ""

    def give_name(self):
        self.name = input("Whats your dogs name?: " + self.name)

    def bark(self):
        print(self.name + " says woof!")
