# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = randint(5,15)
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = randint(10,20)
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
        
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = randint(15,35)
        self._color = 'черный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + 'x' + str(y)
        self.set_answer(x * y)
        return self.__quest

class DifferentialDragon(Dragon):
    def __init__(self):
        self._health = 50
        self._attack = randint(10,15)
        self._color = 'дифференциальный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        z = randint(0,5)
        self.__quest = "(" + str(x) + "x^" + str(y) + ")' at point x=" + str(z)  
        if y-1 > 0 :
            self.set_answer(x*y*(z**(y-1)))
        else:
            self.set_answer(x)
        return self.__quest

class MythrilDragon(Dragon):
    def __init__(self):
        self._health = 50
        self._attack = randint(5,10)
        self._color = 'мифриловый'

    def question(self):
        x = randint(0,10)
        self.__quest = 'guess number in range (0;10)'
        self.set_answer(x)
        return self.__quest



enemy_types = [GreenDragon, RedDragon, BlackDragon, DifferentialDragon, MythrilDragon]
