from dog import Dog_Class #From the file dog.py, import the Dog_Class
import time


mydog = Dog_Class() # Classes

mydog.give_name()

mydog2 = Dog_Class()

mydog2.give_name()

while True:
    mydog.bark()
    time.sleep(1)
    mydog2.bark()
    time.sleep(1)