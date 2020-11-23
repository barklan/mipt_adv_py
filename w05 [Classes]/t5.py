
class Mother:
    __name = "unknown"

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_str(self):
        return f"Name: {self.get_name()}\n---"
    
    def __str__(self):
        return self.get_str()


class Daughter(Mother):
    __mother = "unknown"
    
    def __init__(self, name, mother):
        super().__init__(name)
        self.__mother = mother
    
    def get_mother(self):
        return self.__mother
    
    def set_mother(self, mother):
        self.__mother = mother

    def get_str(self):
        return f"Name: {self.get_name()}; Mother: {self.get_mother()}\n---"
