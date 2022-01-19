class Cat:
    def __init__(self, name, age, color): # Initializing attributes
        self.name = name
        self.age = age
        self.color = color
    def eat(self):  #Function that need an attributes to work
        #subject that is needed in petrleum
        print(f"{self.name} is now eating.")
    def cuddling(self):
        print(f"{self.name} is now cuddling.")
        if self.color == "Orange":
            print("Usually after cuddling, orange cat want to fight with other cat")

my_cat = Cat('Bruno', 2, 'Orange')
print(f"My cat's name is {my_cat.name}.")
print(f"My cat is {my_cat.age} years old.")
my_cat.eat()
my_cat.cuddling()
print(f"My cats name is {my_cat.name}, my cat is {my_cat.age} years old. The color is {my_cat.color}")