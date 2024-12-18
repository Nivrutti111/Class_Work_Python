# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} bark"

# Another child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# Create instances of child classes
dog = Dog("Boddy")
cat = Cat("Whiskers")

# Call the methods
print(dog.speak()) # output: Buddy barks
print(cat.speak()) # output: Whiskers meos
