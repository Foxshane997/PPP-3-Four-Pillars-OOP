# Person Class
class Person:
    def __init__(self, in_name, in_age):
        self.name = in_name
        self.age = in_age
      
    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

# Zoo Class
class Zoo:
    def __init__(self, name="Local Zoo"):
        self.name = name
        self.animals = []
        self.customers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{self.name} has a(n) {animal}")

    def add_animals(self, animals):
        self.animals.extend(animals)
        print(f"{self.name} has many animals")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"{customer} has entered {self.name}")

    def remove_customer(self, customer):
        self.customers.remove(customer)
        print(f"{customer} has left {self.name}")

    def visit_animals(self):
        for a in self.animals:
            print(f"Visiting {a.get_name()}")
            a.make_noise()
            a.eat_food()

# Animal Class
class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def make_noise(self):
        raise NotImplementedError("Subclasses should implement this!")

    def eat_food(self):
        raise NotImplementedError("Subclasses should implement this!")

# Fish Class
class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name} makes bubbling noises.")

    def eat_food(self):
        print(f"{self.name} eats fish flakes.")

# Bird Class
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name} chirps melodiously.")

    def eat_food(self):
        print(f"{self.name} pecks at seeds.")

# Chimp Class
class Chimp(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name} hoots and hollers.")

    def eat_food(self):
        print(f"{self.name} munches on fruits and nuts.")

# Customer Class
class Customer(Person):
    def __init__(self, in_name, in_age):
        super().__init__(in_name, in_age)
        self.has_ticket = False
        self.is_in_zoo = False

    def buy_ticket(self):
        self.has_ticket = True
        if self.age < 12:
            print(f"{self.name} has purchased a child's ticket.")
        else:
            print(f"{self.name} has purchased an adult's ticket.")

    def enter_zoo(self, zoo):
        if self.has_ticket:
            self.has_ticket = False
            zoo.add_customer(self)
            self.is_in_zoo = True
            print(f"{self.name} has entered the zoo.")
        else:
            print(f"{self.name} needs a ticket before entering the zoo.")

    def exit_zoo(self, zoo):
        if self.is_in_zoo:
            self.is_in_zoo = False
            zoo.remove_customer(self)
            print(f"{self.name} has exited the zoo.")
        else:
            print(f"{self.name} is not in the zoo.")

# Example usage
zoo = Zoo()
fish = Fish("koi")
bird = Bird("Raven")
chimp = Chimp("Monkey")

zoo.add_animal(fish)
zoo.add_animal(bird)
zoo.add_animal(chimp)

customer = Customer("Shane", 24)
customer.buy_ticket()
customer.enter_zoo(zoo)

zoo.visit_animals()

customer.exit_zoo(zoo)

