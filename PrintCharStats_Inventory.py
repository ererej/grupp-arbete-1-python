import os
import keyboard
import random as RND
import math
from termcolor import colored
import roman
difficulty = 1

screen1 = ""
doorSet = [0, 0, 0]
isCombat = False
isTresure = False


doorDescriptions = [[" Istället för ett vanligt handtag så har den första dörren en enorm tändsticka som handtag.", " Den andra dörren verkar långsamt bli mindre, som om den försvinner på samma sätt trä försvinner när det brinner.", " Den tredje dörren verkar vara gjord utav kol."], 
[" En stor istapp hänger från den första dörrens handtag.", " Den andra dörren ser exakt ut som en snöflinga.", " Den tredje dörren verkar vara gjord av is."], 
[" Den första dörren verkar ha en dolk istället för ett handtag, bäst att inte ta i den vassa delen."," Den andra dörren har formen av en upp-och-ner vänd sköld."," Den tredje dörrens utsida verkar se ut som man smälte ihop en stor mängd olika vapen."], 
[" Den första dörren har en linjal istället för ett handtag."," Den andra dörren har en form som liknar grafen f(x)= -x**2 + 8x i intervallet 0 <= x <= 8."," Den tredje dörren ser ut att vara gjord linjaler, pennor och sudd."]]


    

class Inventory():
    def __init__(self):
        self.items: list[Item] = []

        self.items.append(Item("item name", 1, 3, [["asd"], ["asgas"], ["hgf"]], False, "Weapon", 3, ["Classy", "really cool"]))
        self.items.append(Item("another item's name", 1, 3, [["asd"], ["asgas"], ["hgf"]], False, "Weapon", 3, ["Classy", "really cool"]))
    
    def PickUpItem(self, foundItem):
        print(f"you found a {foundItem.name}")
        print(PrintInventory(False)) #ska byttas ut till att printa inventoryt med all data när den delen av funktionen är klar!
        if len(player.inventory.items) < 6:
            keybinds_string = f" [{len(player.inventory.items)+1}] to add the item to your inventory"
        else:
            keybinds_string = f" [1-{len(player.inventory.items)}] to replace an item i your iventory with the new item"
        keybinds_string += "\n [0] to discard the item and move on"
        print(keybinds_string)
        key = Input()
        #väntar på en valid input
        while key not in ['0','1','2','3','4','5','6'] or int(key) > len(player.inventory.items)+1:
            key = Input()
        
        if key == "0":
            return
        if len(player.inventory.items) < 6 and int(key) == len(player.inventory.items)+1:
            self.items.append(foundItem) #ska troligen använda items.ItemPickup
        else:
            self.items[int(key)-1].ItemDrop()
            self.items.append(foundItem) # kanske ska lägga till att den lägger till det nya itemet i samma slot 



class Player():
    def __init__(self, health, maxhealth, strength):
        #innehåller all data om spelaren.
        self.level = 1
        self.exp = 0
        self.exp
        self.health = math.floor(health / difficultyMap[difficultyIndex][0])
        self.maxhealth = maxhealth
        self.strength = strength
        self.inventory = Inventory()
        self.elements = [[], [], []]

# Damage types: Physical (swords, clubs, nunchucks), Fire (lava, dragon's breath), Water (ice cannon, snowstorm, scroll of tsunami), and more!

# the elements variable contains a list. 1: Take double damage of this type. 2: Take half damage of this type. 3: The monster deals this damage type.
class Monster():
    def __init__(self, monsterName, strength, health, elements: list[list[str]], enterDesc, attackMoveDesc, deathDesc):
    
        # Denna kod executar när monstret skapas. Här ska olika variabler som namn etc etc skapas, och stats slumpmässigt väljas.
        self.name = monsterName

        self.strength = math.ceil(RND.randint(int(strength * 0.7), int(strength * 1.3) * difficulty))
        self.health = math.ceil(RND.randint(int(health * 0.7), int(health * 1.3) * difficulty))
        self.elements = elements


        self.enterDesc = enterDesc
        self.attackMoveDesc = attackMoveDesc        
        self.deathDesc = deathDesc


class Item():
    def __init__(self, name, strength, health, elements, consumable: bool, itemType, power, boostTypes: list):

        self.name = name

# These are stats given to the player who holds the item.
        self.strength = strength
        self.health = health

# These are values critical to defining the functionality of the item. Element does not matter for pots.
        self.elements = elements
        self.consumable = consumable
        self.itemType = itemType

# Stats important for the functionality of specific items.
        self.power = power
        self.boostTypes = boostTypes

    def ItemPickup(self):
        player.health += self.health
        player.maxhealth += self.health
        player.strength += self.strength

        player.inventory.items.append(self)

    def ItemDrop(self):
        
        player.maxhealth -= self.health
        player.strength -= self.strength

        player.inventory.items.remove(self)


    def CombatActive(self, monster: Monster):

        
        if self.consumable == True:
            self.ItemDrop()

        # Weapons deal (player strength * damageMultiplier) damage of the item's type. Monsters can 
        if self.itemType == "weapon":

            damage: float = player.strength

            for i in monster.elements[0]:
                if monster.elements[0][i] in self.elements:
                    damage *= 2

            for i in monster.elements[1]:
                if monster.elements[0][i] in self.elements:
                    damage /= 2
            
            monster.health -= math.ceil(damage * self.power)
        
        if self.itemType == "pot":
            player.health += self.power

        if self.itemType == "boost":
            player.elements.append()

#the diffirent groups represent different elements. Group 0: fire. Group 1: ice. Group 2: Knighs/weaponry. 3: lärare
#items have 8 paramiters: name, strength, health, elements, consumable, itemType, power, boostTypes

itemDictionary = {
    0: [["Fire item place holder1", 2, 1, 3, True, "weapon", "n/a", "n/a"], ["Fire item place holder2", 2, 1, 3, True, "weapon", "n/a", "n/a"]],
    1: [["Ice item place holder1", 2, 1, 3, True, "weapon", "n/a", "n/a"], ["iqce item place holder2", 2, 1, 3, True, "weapon", "n/a", "n/a"]],
    2: [["Knight item place holder1", 2, 1, 3, True, "weapon", "n/a", "n/a"], ["knight item place holder2", 2, 1, 3, True, "weapon", "n/a", "n/a"]],
    3: [["Exam awnser key", 2, 1, 3, True, "weapon", "n/a", "n/a"], ["teacher item place holder", 2, 1, 3, True, "weapon", "n/a", "n/a"]],
}  
    

# This dictionary contains all data on different monster types. They are sorted into different groups. Group 0: fire. Group 1: ice. Group 2: Knighs/weaponry. 3: lärare

# Tresures are on horizontal index 0
# Tresures have 3 paramiters: Name(idk why but why not (deleate it later if i dont need it)), enter_discription, exit_discription 

# Monster finns på horizontal index 2-4.
# Monster har 6 in-parameters: namn, str, hp, och tre descriptions. 
# Descriptions ska vara om entry i rummet, när monstret attakerar, när monstret dör

encounterDictionary = {
    0: [["the lava pool", " place holder enter disc", "place holder exit disc"], 
        [""], 
        ["THE FIRE SLIME", 1, 6, [[], [], []], "En slemmig, sfärisk varelse som dessutom brinner står framför dig!", "Monstret hoppar in i dig! Lyckligtvis så skadar inte dens kropp dig. Dock gör lågorna det.", "Lågorna på monstret slocknar, och det stelnar till och blir orörligt."], 
        ["", 0, 0, [[], [], []], "", "", ""], 
        ["dragon"], 0, 0, [[], [], []], "", "", ""],
    1: [["place holder tresure", " place holder enter disc", "place holder exit disc"], 
        [""], 
        ["THE MAD SNOWMAN", 4, 3, [[], [], []], "En snögubbe står framför dig! Han verkar dock inte glad att se dig.", "Snögubben kastar en snöboll på dig! Det skadar dig inte, men dock så gör kniven han kör in i din arm det.", "Snögubbens huvud och faller till marken, och ingen mer rörelse händer."], 
        ["THE FROZEN SPIRIT", 0, 0, [[], [], []], "", "", ""], 
        ["THE GLACIER GOLEM"], 0, 0, [[], [], []], "", "", ""],
    2: [["place holder tresure", " place holder enter disc", "place holder exit disc"], 
        [""], 
        ["THE RIDER IN THE DARK", 0, 0, [[], [], []], "", "", ""],
        ["", 0, 0, [[], [], []], "", "", ""], 
        ["THE THOUSAND-PIERCED BEAR", 0, 0, [[], [], []], "", "", ""]],
    3: [["Teacher desk drawer", " You enter the port and find an empty classroom. You follow your natural instinct and start looting the teachers desk for usefull items.", "you close the drawer and quickly run out of the class room to not get cougt red handed"], 
        [""], 
        ["JESPER ENGELMARK", 0, 0, [[], [], []], "", "", ""], 
        ["ANNIKA WESTIN", 0, 0, [[], [], []], "", "", ""], 
        ["MARTIN LOMAN", 0, 0, [[], [], []], "", "", ""]]
}


def Input():
    keyboard.read_key()

    returnedKey = keyboard.read_key()

    return returnedKey.lower()

def PrintHelpMenu():
    os.system('cls')
    print("\n\nHow to play: \n   1: Use items strategically to defeat monsters etcetcetc \n   2: eznella plz do not hold keys plzzz \n\nKeybinds:\n   [R]: Brings up this menu \n   [I]: Opens the inventory\n   [1/2/3]: Enter a room through chosen door")
    while keyboard.read_key() != 'q':
        pass
    os.system("cls")

difficultyMap = [[1, "nuuuuub"], [1.2, "normal"], [1.4, "martin going godmode"]]
difficultyIndex = 1

def Enter(difficultyIndex):


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
            os.system("cls")
            Main()

def Combat(element):
    os.system('cls')
    print("this is combat") #temp
    isCombat = True
    # Grams stats for monster. Randomized monster level. Max ceil scales as percentage as player level increases. lvl 10 is max lvl as of writing.

    try:
        MStats : list = list(encounterDictionary[element])[RND.randint(2, math.floor((player.level / 10) * (len(encounterDictionary[element]) - 2)))]
    except:
        MStats: list = list(encounterDictionary[element])[2]

    encounteredMonster = Monster(MStats[0], MStats[1], MStats[2], MStats[3], MStats[4], MStats[5], MStats[6])

    while (encounteredMonster.health > 0 and player.health > 0):
        print(encounteredMonster.enterDesc)

        key = Input()
        while key not in ['1','2','3','4','5','6'] or int(key) > len(player.inventory.items):
            key = Input()
        
        usedItem = player.inventory.items[int(key) - 1]

        print(f"Du använde {usedItem.name}!")

        usedItem.CombatActive(encounteredMonster)

        

        pass



        isCombat = False
    Input()


def Treasure(element):
    os.system("cls")
    isTresure = True
    print("you found a tresure")
    print(encounterDictionary[element][0][1])
    
    ItemStats: list = list(itemDictionary[element])[RND.randint(0, len(itemDictionary[element])-1)]
    foundItem = Item(ItemStats[0], ItemStats[1], ItemStats[2], ItemStats[3], ItemStats[4], ItemStats[5], ItemStats[6], ItemStats[7])
    player.inventory.PickUpItem(foundItem)
    os.system("cls")
    print(encounterDictionary[element][0][2] + "\n")


    isTresure = False


def Trap(element):
    print('you encoundered a trap')
    Input()
    os.system("cls")


def Main():
    
    while(True):
        #os.system('cls')
        
        screen1 = f"I nästa sal ser du tre portar... "

        doorSet = [0, 0, 0]
        for i in range(1, len(doorSet) + 1):
            doorSet[i-1] = ( RND.randint(0,3) )
            screen1 += '\n'*2 + f"[{i}]" + list( doorDescriptions[ doorSet[i-1] ] )[i - 1]
 
        print(screen1 + "\n"*3 + PrintCharStats())
        
        key = ''
        while key not in ['r', 'q', '1', '2', '3']:
            key = Input()

        if key == "r": 
            PrintHelpMenu()

        if key == 'q':
            break

        if key in ['1', '2', '3']:
            
            encounterStyle = RND.randint(1, 5)

            if(encounterStyle == 1):

                Treasure(doorSet[int(key)-1])

            elif(encounterStyle == 2):

                Trap(doorSet[int(key)-1])

            else:

                Combat(doorSet[int(key)-1])

        
def PrintInventory(allData: bool):
    itemNames = []
    charInventory = ""
    for i in range(0, len(player.inventory.items)):
        itemNames.append((player.inventory.items[i]).name)
    for i in range (0, 6 - len(player.inventory.items)):
        itemNames.append(".........")

    if allData == True:
        pass
    else:

        for i in range(0, len(itemNames)):

            if isCombat or isTresure:
                charInventory += "^──" + f"[{i + 1}]" + "─"*(len(itemNames[i]) - 3)
            else:
                charInventory += "^──" + "─"*len(itemNames[i])




        charInventory += "╷ \n| "

        #lägger till item namen till stränge
        for i in range(0, len(itemNames)):
            charInventory += itemNames[i] + " | "
        
        charInventory += "\n"
        #lägger till ett till långt sträck till stringen

        for i in range(0, len(itemNames)):
            charInventory += "╵──" + "─"*(len(itemNames[i]))
        charInventory += "╵"
        return charInventory

def PrintCharStats():
    charStats = (colored("Health: [" + '■'*(player.health) + ' '*(player.maxhealth-player.health) + "] ", "red") + colored(f"Strength: {player.strength} ", "yellow") + colored(f"Level: {roman.toRoman(player.level)} ", "green") + "\n")
    charStats += PrintInventory(False)
    return charStats
        

player = Player(7, 10, 4)

Enter(difficultyIndex)

