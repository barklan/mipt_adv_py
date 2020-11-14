# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice
import math


class Enemy(Attacker):
    _health = 10
    _cheat_code = "Thisisglobalcheatcode"

    def set_answer(self, answer):
        self.__answer = answer
    
    def check_answer(self, answer):
        return answer == self.__answer

    def get_cheat_code(self):
        return self._cheat_code


# Generates random enemy
def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


# Populates enemy_list with random enemies with length of enemy_number
def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def __init__(self, health, color, cheat_code):
        self._health = health
        self._color = color
        self._cheat_code = cheat_code


class GreenDragon(Dragon):
    def __init__(self):
        super().__init__(200, 'green', 'greencheatcode')
        self._attack = randint(5,15)


    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        super().__init__(200, 'red', 'redcheatcode')
        self._attack = randint(10,20)

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

   
class BlackDragon(Dragon):
    def __init__(self):
        super().__init__(200, 'black', 'blackcheatcode')
        self._attack = randint(15, 35)

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + 'x' + str(y)
        self.set_answer(x * y)
        return self.__quest


class DifferentialDragon(Dragon):
    def __init__(self):
        super().__init__(50, 'differential', 'differentialcheatcode')
        self._attack = randint(10,15)

    def question(self):
        x = randint(1, 10)
        y = randint(1, 10)
        z = randint(0, 5)
        self.__quest = "(" + str(x) + "x^" + str(y) + ")' at point x=" + str(z)  
        if y-1 > 0 :
            self.set_answer(x * y * (z ** (y-1)))
        else:
            self.set_answer(x)
        return self.__quest


class MythrilDragon(Dragon):
    def __init__(self):
        super().__init__(50, 'mythril', 'mythrilcheatcode')
        self._attack = randint(5,10)

    def question(self):
        x = randint(0,10)
        self.__quest = 'guess number in range (0;10)'
        self.set_answer(x)
        return self.__quest


def get_factor_list(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(int(i))
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(int(n))
   return primfac


class Troll(Enemy):
    _color = 'troll (not dragon)'

    def __init__(self):
        self._attack = randint(5,10)
        self._color = 'troll (not dragon)'

    def question(self):
        x = randint(4,15)
        self.__quest = f'type the the prime factorization of {x} without spaces'
        self.set_answer(int(''.join(map(str, get_factor_list(x)))))
        return self.__quest


enemy_types = [GreenDragon, RedDragon, BlackDragon, DifferentialDragon, MythrilDragon, Troll]
