#Class example in Java

#class Animal {
#    String name;
#    int age;

#    void eat() {
#        System.out.println("Animal is eating");
#    }
#}

#Class example in Python

class Animal:
    
    name = "tiger"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"Animal {self.name} & {Animal.name} aged {self.age} are eating")

#self is a reference to the current instance of the class, like "this" in Java. It is written explicitly in Python. 
#It is used for every instance method in the class. 
#It allows us to access the attributes and methods of the class within the class itself. 

#Creating an instance of the Animal class

a = Animal("Lion", 5)
a.eat()