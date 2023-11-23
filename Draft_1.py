# The assembly line
import os
import keyboard 
import random as RND
import math

difficulty = 1

descriptionText = ""



class Item():
    pass

class Inventory():
    pass

class Player():
    pass

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
difficulties = {
    1: "noob mode",
    1.2: "Normal",
    1.4: "Martin"
}

CanInput = True
def Input():
    keyboard.read_key() 

    returnedKey = keyboard.read_key()

    return returnedKey.lower()

def Enter():
    os.system('cls')

    print(f"Välkommen till Dungeon Delver Monkey, din favoritdejtingapp!" + "\n"*4 + "Difficulty: " + difficulties[difficulty] + "\n"*4 + "For rules and keybinds, press [R] at any point in the game" + "\n"*4 + "Press [S] to start" + "\n"*4 + "Press [Q] to rage quit")
    key = Input()

    if key == "q":
        0/0

Enter()