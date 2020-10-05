
class Animal:
    __name = "unknown"
    __age = "unknown"
    __description = "-"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description

    def get_str(self):
        return f"Name: {self.get_name()}; Age: {self.get_age()}; \
                        Description: {self.get_description()}\n---"
    
    def __str__(self):
        return self.get_str()


class Zebra(Animal):
    __number_of_legs = 4
    
    def __init__(self, name, age, number_of_legs):
        super().__init__(name, age)
        self.__number_of_legs = number_of_legs


class Dolphin(Animal):
    def swim_across_the_ocean(self):
        print('Swimming...')
    pass

# z = Zebra("Zebra1", "118", number_of_legs=5)
# z.set_description("This is Zebra1 - the best zebra there is. It has 5 legs!")

# d = Dolphin("Jonny", "4")
# d.set_description("This is Dolphin Jonny - he is 5yr old.")

# print(z)
# print(d)
