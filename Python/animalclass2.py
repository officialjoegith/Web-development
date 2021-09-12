# Class
# Build a student class
class Animals:

    def __init__(self, name, lifespan, gender, breed, size):
        self.name = name
        self.lifespan = lifespan
        self.gender = gender
        self.breed = breed
        self.size = size

    def eat(self):
        print(f"{self.name} consumes food in large quantity")

animal1 = Animals("Chelsea", 2, "F", "Bull Dog", "50kg")
animal2 = Animals("Lucky", 5, "M", "Pit Bull", "65kg")

print(animal1.name)
print(animal2.breed)

animal1.eat()

#Inheritance
class Dog(Animals):
    def __init__(self, name, lifespan, gender, breed, size ):
        Animals.__init__(self, name, lifespan, gender, breed, size)

    def barks(self):
        print(f"{self.name} barks whenever its sees a stranger")

    
dog = Dog("Pixie", 1, "F", "Alsatian", "35kg")
dog.barks()


class Cat(Animals):
    def __init__(self, name, lifespan, gender, breed, size ):
        Animals.__init__(self, name, lifespan, gender, breed, size)

    def meows(self):
        print(f"{self.name} meows whenever angry")

    
cat = Cat("Lia", 2, "F", "Baby", "25kg")
cat.meows()


class Fish(Animals):
    def __init__(self, name, lifespan, gender, breed, size ):
        Animals.__init__(self, name, lifespan, gender, breed, size)

    def swims(self):
        print(f"{self.name} swims alot to calm nerves")


fish = Fish("Fin", 1, "F", "Cat Fish", "5kg")
fish.swims()


