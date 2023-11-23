# The assembly line
import os
import keyboard 
import random as RND
import math

difficulty = 1

descriptionText = ""



class Monster():
    def __init__(self, monsterName, strength, health, weakness: list, attackMoveDesc, deathDesc):
        
        # Denna kod executar när monstret skapas. Här ska olika variabler som namn etc etc skapas, och stats slumpmässigt väljas.
        self.name = monsterName

        self.strength = math.ceil(RND.randint(strength * 0.7, strength * 1.3) * difficulty)
        self.health = math.ceil(RND.randint(health * 0.7, health * 1.3) * difficulty)

        self.weakness = weakness
        self.attackMoveDesc = attackMoveDesc
        self.deathDesc = deathDesc

# This dictionary contains all data on different monster types. They are sorted into different groups. Group 1 contains fire monsters, 
# group 2 shadow monsters, group 3 martial monsters, group 4 acid monsters, and group 5 stereotypes.
monsterDictionary = {
    1: [[], [], []],
    2: [[], [], []],
    3: [[], [], []],
    4: [[], [], []],
    5: [[], [], []]
}

CanInput = True
def Input():
    discardKey = keyboard.read_key() #behöver vi ens asigna en variabel till keyboard.read_key()?

    returnedKey = keyboard.read_key()

    return returnedKey

def Enter():

    # När spelaren vunnit/förlorat spelet återvänder hen hit...
    while (True):

        key = Input()
        
        print(key)

        if (key == "d"):
            print("hej")
        elif (key == "p"):
            print("nej")

Enter()