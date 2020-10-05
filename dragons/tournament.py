# coding: utf-8
# license: GPLv3
from hero import Hero
from random import randint, choice
from enemies import generate_enemy_list
import sys



def humanizer():
    while True:
        try:
            answer = int(input())
        except ValueError:
            print('Type a number, you shitface!')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('You are fighting', dragon._color, 'dragon!')
        while dragon.is_alive() and hero.is_alive():
            print('Question:', dragon.question())
            
            inp = input('Answer:')
            if inp == "exit":
                sys.exit()
            elif inp == dragon.get_cheat_code():
                dragon._health = 0
                break
            else:
                try:
                    answer = int(inp)
                except ValueError:
                    answer = humanizer()

                
            if dragon.check_answer(int(answer)):
                hero.attack(dragon)
                hero._experience += randint(0,5)
                print('Right! \n** you hurted dragon **')
            else:
                dragon.attack(hero)
                hero._experience -= randint(0,5)
                print('Wrong! \n** you have been hit... **')
        
        ''' 
        If we are here that means either we killed the dragon -
            in that case we naturaly print the next message;
        or we died - in that case the dragon is still alive and
            we don't want to print the next message and we want to exit
            immediatly and expect hero.is_alive to return False
        '''

        if dragon.is_alive():
            break
        print('Dragon', dragon._color, 'defeated!\n')


    if hero.is_alive():
        print('Congrats, you won')
        print('Your expirience:', hero._experience)
    else:
        print('Sadly, you lost...')


def start_game():
    try:
        print('Welcome to arithmetic dragons!')
        print('To exit the game - type `exit` at any time')
        print('Identify yourself: ', end = '')
        hero = Hero(input())

        enemy_number = 3
        enemy_list = generate_enemy_list(enemy_number)
        assert(len(enemy_list) == 3)
        print('You see', enemy_number, 'dragons!')
        game_tournament(hero, enemy_list)

    except EOFError:
        print('This is EOF message. You cannot submit any more answers.')
