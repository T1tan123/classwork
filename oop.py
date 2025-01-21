class Animal:
    def __init__(self, name):
        self.name = name

        def speak(self):
            return f"{self.name} издает звуки"

class Dog(Animal):
    def speak(self):
        return f"{self.name} гавкает"

class Cat(Animal):
    def speak(self):
        return f"{self.name} мяукает"


animals = [Dog('bobik'),Cat('olivia') ]
for a in animals:
    print(a.speak())
