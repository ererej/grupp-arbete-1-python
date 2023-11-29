import os
import keyboard
import random as RND
import math
from termcolor import colored
difficulty = 1

screen1 = ""
doorSet = [0, 0, 0]


doorDescriptions = [[" Hetta emnerar från den första.", " Den andra har ett fönster, men du kan inte se in i rummet eftersom du blir bländad av elden där inne.", " Den tredje dörren är gjord utav kol."], 
[" En stor istapp hänger från den första dörrens handtag.", " colddoor_2", " Den tredje dörren verkar vara gjord av is."],  
[" weapondoor_1"," weapondoor_2"," Den tredje dörren verkar vara gjord för att efterlikna en mängd olika vapen.",],
[" teacherdoor_1"," teacherdoor_2"," Den tredje dörren verkar vara gjord linjaler, pennor och sudd.",]]

class Item():
    def __init__(self, name, strength, health, type,):
        self.name = name
        self.strength = strength
        self.health = health
        self.type = type

class Inventory():
    def __init__(self):
        pass

class Player():
    def __init__(self, level, health, strenght):
        #innehåller all data om spelaren.
        self.level = level
        self.health = health
        self.strenght = strenght
        self.inventory = Inventory()

class Monster():
    def __init__(self, monsterName, strength, health, weakness: list, enterDesc, attackMoveDesc, deathDesc):
        # The weakness list contains its offensive and defensive weakness (in that order)
        # Denna kod executar när monstret skapas. Här ska olika variabler som namn etc etc skapas, och stats slumpmässigt väljas.
        self.name = monsterName

        self.strength = RND.randint(strength * 0.7, strength * 1.3) * difficulty
        self.health = RND.randint(health * 0.7, health * 1.3) * difficulty

        self.weakness = weakness
        self.attackMoveDesc = attackMoveDesc
        self.deathDesc = deathDesc
        self.enterDesc = enterDesc

# This dictionary contains all data on different monster types. They are sorted into different groups. Group 0: fire. Group 1: ice. Group 2: Knighs/weaponry. 3: lärare
monsterDictionary = {
    0: [[], [], []],
    1: [[], [], []],
    2: [[], [], []],
    3: [['Jesper Engelmark'], ['Annika Westin'], ['Martin Loman']]
}

def Input():
    keyboard.read_key()

    returnedKey = keyboard.read_key()

    return returnedKey.lower()

def PrintHelpMenu():
    os.system('cls')
    print("\n\nHow to play: \n   1: Use items strategically to defeat monsters etcetcetc \n   2: eznella plz do not hold keys plzzz \n\nKeybinds:\n   [R]: Brings up this menu \n   [I]: Opens the inventory\n   ")
    while keyboard.read_key() != 'q':
        pass

difficultyMap = [[1, "nuuuuub"], [1.2, "normal"], [1.4, "martin going godmode"]]

def Enter():
    difficultyIndex = 1

    while(True):
        os.system('cls')

        currentDifficulty: list = difficultyMap[difficultyIndex]
    
        screen1 = colored("""
.----.   .--.   .-.  .-. .----.    .-. .-.   .--.   .-.  .-. .----.    .----. .---.  .---.   .---.  .---.  
| |--'  / {} \  }  \/  { } |__}    |  \{ |  / {} \  }  \/  { } |__}    } |__} } }}_} } }}_} / {-. \ } }}_} 
| }-`} /  /\  \ | {  } | } '__}    | }\  { /  /\  \ | {  } | } '__}    } '__} | } \  | } \  \ '-} / | } \  
`----' `-'  `-' `-'  `-' `----'    `-' `-' `-'  `-' `-'  `-' `----'    `----' `-'-'  `-'-'   `---'  `-'-'  """, 'yellow') + "\n"*3 + "Difficulty: " + currentDifficulty[1] + "\n"*3 + "For rules and keybinds, press [R] at any point in the game" + "\n"*3 + colored("Press [S] to start", "green") + "\n"*3 + colored("Press [Q] to rage quit", "red")
        print(screen1)
        key = Input()

        if key == "q":
            exit()

        if key == "r":
            PrintHelpMenu()

        if key == "d":
            difficultyIndex -= 1
            if difficultyIndex == -1:
                difficultyIndex = len(difficultyMap)-1
        if key == "s":
            Main()

def Combat(element):
    pass

def Main():
    
    while(True):
        os.system('cls')
        
        screen1 = f"I nästa sal ser du tre portar... "

        doorSet = [0, 0, 0]
        for i in range(1, len(doorSet) + 1):
            doorSet[i-1] = ( RND.randint(0,3) )
            screen1 += '\n'*2 + list( doorDescriptions[ doorSet[i-1] ] )[i - 1]
 
        print(screen1 + "\n"*3 + PrintCharStats())
        
        key = ''
        while key not in ['r', 'q', '1', '2', '3']:
            key = Input()

        if key == "r": 
            PrintHelpMenu()

        if key == 'q':
            break

        if key in ['1', '2', '3']:
            Combat(doorSet[int(key)] )

        

        

def PrintCharStats():
    return (colored("Health: [" + '■ '*(player.health-1) + "■] ", "red") + colored(f"Strength: {player.strenght} ", "yellow") + colored(f"Level: {player.level} ", "green") + "\n" + "-"*31 + "\n|inventory preview place holder" + "|\n" + "-"*31 + "\n")


player = Player(0, 10, 4)

Enter()

