# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Creating an object of the child class
dog = Dog("Buddy")
dog.speak()  # Outputs: Buddy says Woof!
