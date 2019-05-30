# build a fruit stand that has a barrel for fruit and fruits have
# a name and price
# you should be able to get the total cost of the barrel given the number of fruits in it
# and their cost.
# a barrel can only hold one fruit type

# make a menu with the print in a dif file
# fruit object
# barrel object


class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Barrel:
    def __init__(self):
        self.fruit_count = 0
        self.fruit_type = None

    def sum_total(self):
        return self.fruit_count * self.fruit_type.price

    def add_fruit(self, fruit):
        if self.fruit_type == fruit.name:
            self.fruit_count += 1
        elif self.fruit_type == None:
            self.fruit_type = fruit
            self.fruit_count += 1
        else:
            return "Invalid barrel for that fruit"


apple = Fruit("Apple", 1.2)
apple_barrel = Barrel()
apple_barrel.add_fruit(apple)
apple_barrel.sum_total()


# # make a menu class that asks the user what to do
# 1 add to a barrel
# 2 get the type of fruit in the barrel
# 3 remove an amount of fruit from the barrel
# 4 reset the barrel, empty it and set it back to None
# 5 exit

# also make the needed barrel methods
# due start of class tomorrow
