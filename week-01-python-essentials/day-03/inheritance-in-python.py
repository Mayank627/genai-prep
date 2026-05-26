class Animal:

    name = "tiger"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"Animal {self.name} & {Animal.name} aged {self.age} are eating")

a = Animal("Lion", 5)
a.eat()


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

d = Dog("Buddy", 3)
d.eat()  # Inherited method from Animal class       
d.bark() # Dog's own method