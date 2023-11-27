# The assembly line
import os
import keyboard 
import random as RND
import math
from termcolor import colored
difficulty = 1

screen1 = ""
screen2 = ""


class Item():
    pass

class Inventory():
    pass

class Player():
    def __init__(self, level:int, health:int, strenght:int):
        self.level = level
        self.health = health
        self.strenght = strenght

class Monster():
    def __init__(self, monsterName, strength, health, weakness: list, enterDesc, attackMoveDesc, deathDesc):
        # The weakness list contains its offensive and defensive weakness (in that order)
        # Denna kod executar när monstret skapas. Här ska olika variabler som namn etc etc skapas, och stats slumpmässigt väljas.
        self.name = monsterName

        self.strength = math.ceil(RND.randint(strength * 0.7, strength * 1.3) * difficulty)
        self.health = math.ceil(RND.randint(health * 0.7, health * 1.3) * difficulty)

        self.weakness = weakness
        self.attackMoveDesc = attackMoveDesc
        self.deathDesc = deathDesc
        self.enterDesc = enterDesc

# This dictionary contains all data on different monster types. They are sorted into different groups. Group 1 contains fire monsters, 
# group 2 shadow monsters, group 3 martial monsters, group 4 acid monsters, and group 5 stereotypes.
monsterDictionary = {
    1: [[], [], []],
    2: [[], [], []],
    3: [[], [], []],
    4: [[], [], []],
    5: [[], [], []]
}

def Input():
    keyboard.read_key() #varför asignde du en varieabel igen?

    returnedKey = keyboard.read_key()

    return returnedKey.lower()

def PrintRules():
    os.system('cls')
    print("\n\nWOWIE THE RULELULES? IVE NO IDEA WHERE THEY WENT, AHAHAHAHHAHHAHHAHAHAHAHAHH IMBTKMSRNBRB EXCEPT I WONT XDDDDDDDD LIP (LAUGHING IN PAIN) press any key to go back to whereever u were also if you hold a key the game lags cuzz the library im using is garbage")
    while keyboard.read_key() != 'q':
        pass

difficultyIndex = 1
difficultyMap = [[1, "nuuuuub"], [1.2, "normal"], [1.4, "martin going godmode"]]

def Enter():

    while(True):
        os.system('cls')

        currentDifficulty: list = difficultyMap[difficultyIndex]
    
        screen1 = colored(f"Välkommen till Dungeon Delver Monkey, din favoritdejtingapp!", 'yellow') + "\n"*3 + "Difficulty: " + currentDifficulty[1] + "\n"*3 + "For rules and keybinds, press [R] at any point in the game" + "\n"*3 + colored("Press [S] to start", "green") + "\n"*3 + colored("Press [Q] to rage quit", "red")
        print(screen1)
        key = Input()

        if key == "q":
            exit()

        if key == "r":
            PrintRules()
        if key == "d":
            difficultyIndex -= 1
        if key == "s":
            doorLoop()



def doorLoop():
     
     while(True):
        os.system('cls')

        screen2 = "du går fram till tre dörrar" + "\n" + "bakom den vänstra dörren finns {door(1).description}" + "\n" + "bakom den mitersta dörren finns {door(1).description}" + "\n" + "bakom den högra dörren finns {door(1).description}" + "\n"*3 + colored("Health: [" + f"{'■'*player.health}"+ "] ", "red") + colored(f"Strength: {player.strenght} ", "yellow") + colored(f"Level: {player.level} ", "green") + "\n" + "-"*31 + "\n|inventory prevju place holder" + "|\n" + "-"*31 + "\n"
        print(screen2)
        key = Input()
        if key == "r": 
            PrintRules()




player = Player(0, 10, 4)

Enter()