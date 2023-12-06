# Team Outrun: the ones that ran out of time

import os
import keyboard
import random as RND
import math
from termcolor import colored
import roman

difficulty = 1

screen1 = ""
doorSet = [0, 0, 0]
global canAct 
canAct = False

ELEMENT_WEAKNESS = 0
ELEMENT_RESISTANCE = 1
ELEMENT_ATTACK_TYPE = 2


doorDescriptions = [[colored(" Istället för ett vanligt handtag så har den första dörren en enorm tändsticka som handtag.", "red"), colored(" Den andra dörren verkar långsamt bli mindre, som om den försvinner på samma sätt trä försvinner när det brinner.", "red"), colored(" Den tredje dörren verkar vara gjord utav kol.", "red")], 
[colored(" En stor istapp hänger från den första dörrens handtag.", "light_cyan"), colored(" Den andra dörren ser exakt ut som en snöflinga.", "light_cyan"), colored(" Den tredje dörren verkar vara gjord av is.", "light_cyan")], 
[colored(" Den första dörren verkar ha en dolk istället för ett handtag, bäst att inte ta i den vassa delen.", "dark_grey"), colored(" Den andra dörren har formen av en upp-och-ner vänd sköld.", "dark_grey"), colored(" Den tredje dörrens utsida verkar se ut som man smälte ihop en stor mängd olika vapen.", "dark_grey")], 
[colored(" The first door has a ruller as the doorhandel", "yellow"), colored(" Behind the secound door you hear the faint buzzing of a procjector", "yellow"), colored(" Den tredje dörren ser ut att vara gjord linjaler, pennor och sudd.", "yellow")]]


    




class Player():
    def __init__(self):
        #innehåller all data om spelaren.
        self.level = 1
        self.exp = 0
        self.exp
        self.maxhealth = 10
        self.health = math.floor(self.maxhealth / difficultyMap[difficultyIndex][0])
        self.strength = 3
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


    

# self: ett visst item. Används troligen inte utanför klassen
# name: Monstrets namn. Används för intro descriptions etcetc
# strength: give the player this amount of strength, empowering their attacks.
# health: Give the player this amount of health, granting them vigor in combat.
# elements: A
# consumable: If set to True, this item will remove itself from the player's inventory upon being used.
# itemType: defines the functionality of the item. Can be a damage-dealing weapon, a healing potion ("pot"), or a 
# resistance potion that halves damage taken from some damage types.
# power: Defines the amount of health restored by healing potions and damage multiplier for weapons.
class Item():
    def __init__(self, name, strength, health, elements, consumable: bool, itemType, power, resistancePotEffects: list):

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
        self.resistancePotEffects = resistancePotEffects

    def ItemPickup(self):
        """hej"""
        player.health += self.health
        player.maxhealth += self.health
        player.strength += self.strength

        player.inventory.items.append(self)

    def ItemDrop(self):
        
        player.maxhealth -= self.health
        player.strength -= self.strength

        player.inventory.items.remove(self)


    def CombatActive(self, monster: Monster):

        # Weapons deal (player strength * damageMultiplier) damage of the item's type. Monsters can 
        if self.itemType == "weapon":

            damage: float = player.strength

            for i in monster.elements[ELEMENT_WEAKNESS]:
                if monster.elements[ELEMENT_WEAKNESS][i] in self.elements:
                    damage *= 2

            for i in monster.elements[ELEMENT_RESISTANCE]:
                if monster.elements[ELEMENT_RESISTANCE][i] in self.elements:
                    damage /= 2
            
            monster.health -= math.ceil(damage * self.power)
        
        if self.itemType == "health potion":
            player.health += self.power

        if self.itemType == "resistance-giver":
            for i in self.resistancePotEffects:
                player.elements[ELEMENT_RESISTANCE].append(self.resistancePotEffects[i])

        if self.consumable == True:
            self.ItemDrop()




class Inventory():
    def __init__(self):
        self.items: list[Item] = []


    
    def PickUpItem(self, foundItem:Item):
        while True:
            os.system("cls")
            print(colored(f"\nYou found {foundItem.name}") + ", a ", colored(f"{foundItem.itemType}\n", "red") + "-type item")
        
            if len(player.inventory.items) < 6:
                keybinds_string = f"[{len(player.inventory.items)+1}] Add the item to your inventory"
            else:
                keybinds_string = f" [1-6] Replace an item in your inventory"
            keybinds_string += "\n[0] discard the item and move on"
            print(keybinds_string)
            print("\n"*2 + PrintCharStats())
            key = Input()
            #väntar på en valid input
            try:
                if len(player.inventory.items) == 6:
                    if int(key) < len(player.inventory.items):
                        break
                if int(key) <= len(player.inventory.items)+1:
                    break
            except:
                if key == "i":
                    PrintInventory()
                pass
            
        if key == "0":
            return
        if len(player.inventory.items) == 6:
            self.items[int(key)-1].ItemDrop()
            foundItem.ItemPickup # kanske ska lägga till att den lägger till det nya itemet i samma slot 
            return
        foundItem.ItemPickup() 
        return
        



itemDictionary = {
    0: [["a fire resistance potion", 0, 1, [], True, "boost", [], []], ["Fire item place holder2", 2, 1, 0, False, "weapon", [], []]],
    1: [["Ice item place holder1", 2, 1, 1, False, "weapon", [], []], ["ice item place holder2", 2, 1, 1, False, "weapon", [], []]],
    2: [["a wooden sword", 2, 0, 2, False, "weapon", [], []], ["knight item place holder2", 2, 1, 2, False, "weapon", [], []]],
    3: [["Exam awnser key", 2, 1, 3, True, "weapon", [], []], ["teacher item place holder", 2, 1, 3, False, "weapon", [], []]],
}  
#the diffirent groups represent different elements. Group 0: fire. Group 1: ice. Group 2: Knighs/weaponry. 3: lärare
#items have 8 paramiters: name, strength, health, elements, consumable, itemType, power, boostTypes    

# This dictionary contains all data on different monster types. They are sorted into different groups. Group 0: fire. Group 1: ice. Group 2: Knighs/weaponry. 3: lärare

# Tresures are on horizontal index 0
# Tresures have 3 paramiters: Name(idk why but why not (deleate it later if i dont need it)), enter_discription, exit_discription 

#traps are horizontal index 1
#traps have 2 paramiters: enterdisc, exitdisc

# Monster finns på horizontal index 2-4.
# Monster har 6 in-parameters: namn, str, hp, och tre descriptions. 
# Descriptions ska vara om entry i rummet, när monstret attakerar, när monstret dör

encounterDictionary = [[["placeholder enter disc", "place holder exit disc"], #The lava pit 
        ["Fire trap", "As you enter the room you hear mechanical sounds coming from the walls before you get enveloped by fire", "You quickly leave the room to avoid burning up."], 
        ["THE FIRE SLIME", 2, 6, [["frost"], ["fire"], ["fire, fire"]], "A slimy, spherical creature that also appears to be on fire stands infront of you!", ["The slime jumps into you! Luckely its body does not hurt. The flames however, does.", "The slime spits out a stream of fire onto you!"], "The flames on the monster extinguish, and it solidifies."], 
        ["DASTARDLY IMP", 6, 8, [["phys"], ["fire"], ["fire","psy"]], "An imp appears! It seems to be quite cruel with its attacks.", ["The imp throws fireballs at you!","The imp casts a spell upon you! It seems like it damaged your mind."], "The imp lets out a shreik, and dies."], 
        ["DRAGON"], 8, 25, [["psy"], ["phys"], ["fire","phys"]], "You spot a formidable dragon standing some distance away. You try to avoid it, but it notices you. Prepare for battle!", ["The Dragon breathes fire at you!","The Dragon slashes its claws at you!"], "The dragon lets out a cry of pain, before falling to the ground dead."],
        [["placeholder enter disc", "place holder exit disc"], 
        ["", ""], 
        ["THE MAD SNOWMAN", 4, 3, [["fire"], ["frost"], ["phys","frost"]], "You notice a snowman in the room. When you go to get a closer look, it wakes to life!", ["The snowman throws a snowball at you! It doesn't hurt you, but then he drives a knife into your arm.", "The snow man throws a water baloon at you! Atleast you think it was water, but it turns out to be filled with liquid nitrogen!"], "The head of the snowman falls to the ground, and there is no more movement."], 
        ["THE FROZEN SPIRIT", 5, 15, [["psy"], ["phys"], ["psy","frost"]], "You enter a room, but it is empty. Then a spirit flies in through the wall!", ["The spirit casts a spell, draining your sanity and mental health.","The spirit causes the vapor in the air to freeze into icicles, then it throws them at you!"], "The sprits vanishes into thin air."], 
        ["THE GLACIER GOLEM"], 14, 8, [["phys"], ["psy"], ["frost","phys"]], "A gargantuan ice golem stands infront of you!", ["The golem cools the area significantly to the point you develop frostbite!","The golem slams you with its giant arm!"], "Cracks appear on the golem moments before it falls apart. Turns out being made of ice made it quite fragile."],
        [["placeholder enter disc", "place holder exit disc"], 
        ["", ""], 
        ["THE DESERTER", 3, 7, [["psy"], ["phys"], ["phys","fire"]], "You spot a soldier infront of you! He seems to have deserted the army he once belonged to.", ["The soldier tries to shoot you with his rifle, but it's jammed. So then he attacks you with it like a club!","The soldier attacks you with a miniature flamethrower!"], "The solder lets out a groan, before falling to the ground motionless"],
        ["THE RIDER IN THE DARK", 2, 25, [["frost"], ["psy"], ["phys","psy"]], "You enter a dimly-lit room. Standing infront of you seems to be a person riding a horse. You aren't to sure of its intentions, but best to attempt to kill it.", ["The rider attacks you with a spear! Or does it? It does not hurt that much...","The rider messes with your mind... in some unknown way. You are not entirely sure what he did, but you don't feel as healthy as before"], "The rider... disapears. It does not vanish, but at the same time it just... Well, it is dead, and you won, and that is what matters."], 
        ["THE THOUSAND-PIERCED BEAR", 10, 35, [["frost"], ["phys"], ["phys, phys"]], "You spot a bear infront of you! Judging by the various weapons stuck in its fur, it seems to be very dangerous!", ["The bear mauls you with its razor-sharp teeth!","The bear thrusts its claws into you like they were daggers!"], "The bear screams in great pain and tries to go for another attack, but falls to the ground dead before it could."]],
        [["You enter the door and find an empty classroom. You follow your natural instinct and start looting the teachers desk for useful items.", "You close the drawer and quickly run out of the classroom to not get caught red-handed."], 
        ["", ""], 
        ["JESPER ENGELMARK", 3, 8, [["phys"], ["psy"], ["phys","psy"]], "", ["",""], ""], 
        ["ANNIKA WESTIN", 6, 12, [["fire"], ["frost"], ["psy","psy"]], "", ["",""], ""], 
        ["MARTIN LOMAN", 12, 24, [["fire"], ["psy"], ["frost","psy"]], "", ["",""], ""]]]


def Input():
    keyboard.read_key()

    returnedKey = keyboard.read_key()

    return returnedKey.lower()

def PrintHelpMenu():
    os.system('cls')
    print("\n\nHow to play: \n   1: Use items strategically to defeat monsters etcetcetc \n   2: eznella plz do not hold keys plzzz \n\nKeybinds:\n   [R]: Brings up this menu \n   [I]: Opens the inventory\n   [1/2/3]: Enter a room through chosen door")
    while keyboard.read_key() != 'q':
        pass

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
`----' `-'  `-' `-'  `-' `----'    `-' `-' `-'  `-' `-'  `-' `----'    `----' `-'-'  `-'-'   `---'  `-'-'  """, 'yellow') + "\n"*3 + "Difficulty: " + currentDifficulty[1] + "\nPress [D] to change difficulty" + "\n"*3 + "For rules and keybinds, press [R] at any point in the game" + "\n"*3 + colored("Press [S] to start", "green") + "\n"*3 + colored("Press [Q] to rage quit", "red")
        print(screen1)
        key = Input()

        if key == "q":
            exit()

        if key == "r":
            PrintHelpMenu()
        
        if key == "i":
            PrintInventory()

        if key == "d":
            difficultyIndex += 1
            if difficultyIndex == len(difficultyMap):
                difficultyIndex = 0
        if key == "s":
            os.system("cls")
            Main()

def Combat(element):
    global canAct
    canAct = True
    os.system('cls')
    print("this is combat") #temp
    # Grams stats for monster. Randomized monster level. Max ceil scales as percentage as player level increases. lvl 10 is max lvl as of writing.

    try:
        MStats : list = list(encounterDictionary[element])[RND.randint(2, math.floor((player.level / 10) * (len(encounterDictionary[element]) - 2)))]
    except:
        # If the player has not yet reached the level 2 monster, it will simply grab the lvl 1 monsters stats. This is because randint function does not accept two identical parameters.
        MStats: list = list(encounterDictionary[element])[2]

    encounteredMonster = Monster(MStats[0], MStats[1], MStats[2], MStats[3], MStats[4], MStats[5], MStats[6])



    while (encounteredMonster.health > 0 and player.health > 0):
        print(encounteredMonster.enterDesc)

        key = Input()
        while key not in ['1','2','3','4','5','6'] or int(key) > len(player.inventory.items):
            key = Input()
        
        usedItem = player.inventory.items[int(key) - 1]
        print(f"You used {usedItem.name}!")
        usedItem.CombatActive(encounteredMonster)
        try:
            attackIndex = RND.randint(0, len(encounteredMonster.attackMoveDesc) - 1)
        except:
            attackIndex = 0

        print(encounteredMonster.attackMoveDesc[attackIndex])

        damage = encounteredMonster.strength

        for i in player.elements[ELEMENT_WEAKNESS]:
            if player.elements[ELEMENT_WEAKNESS][i] in encounteredMonster.elements[ELEMENT_ATTACK_TYPE][attackIndex]:
                damage *= 2

        for i in player.elements[ELEMENT_RESISTANCE]:
            if player.elements[ELEMENT_RESISTANCE][i] in encounteredMonster.elements[ELEMENT_ATTACK_TYPE][attackIndex]:
                damage /= 2

        player.health -= damage




        
    
        



    Input()


def Treasure(element):
    os.system("cls")

    ItemStats: list = list(itemDictionary[element])[RND.randint(0, len(itemDictionary[element])-1)]
    foundItem = Item(ItemStats[0], ItemStats[1], ItemStats[2], ItemStats[3], ItemStats[4], ItemStats[5], ItemStats[6], ItemStats[7])
    player.inventory.PickUpItem(foundItem)

    print(encounterDictionary[element][0][2] + "\n"*2 + "Press any key to continue!")
    Input()




def Trap(element):
    os.system('cls')
    print(encounterDictionary[element][1][0])
    damageTaken = RND.randint(1, 2)
    player.health -= damageTaken
    print(f"You took {damageTaken}damage")
    if player.health <= 0:
        pass #game over screen?
    print(encounterDictionary[element][1][1])
    Input()


def Main():
    
    while(True):
        os.system('cls')
        
        screen1 = f"In the next room you see three doors"

        doorSet = [0, 0, 0]
        for i in range(1, len(doorSet) + 1):
            doorSet[i-1] = ( RND.randint(0,3) )
            screen1 += '\n'*2 + f"[{i}]" + list( doorDescriptions[ doorSet[i-1] ] )[i - 1]
 
        print(screen1 + "\n"*3 + PrintCharStats())
        
        key = ''
        while key not in ["i", 'r', 'q', '1', '2', '3']:
            key = Input()

        if key == "r": 
            PrintHelpMenu()

        if key == "i":
            PrintInventory()

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

        
def PrintInventory():
    os.system("cls")
    inventoryString = ""
    for item in player.inventory.items:
        inventoryString = f"{item.name}, "
    print(inventoryString)
    while keyboard.read_key() != 'q':
        pass
    return

def PrintCharStats():
    global canAct
    charStats = (colored("Health: [" + '■'*(player.health) + ' '*(player.maxhealth-player.health) + "] ", "red") + colored(f"Strength: {player.strength} ", "yellow") + colored(f"Level: {roman.toRoman(player.level)} ", "green") + "\n")
    itemNames = []

    for i in range(0, len(player.inventory.items)):
        itemNames.append((player.inventory.items[i]).name)
    for i in range (0, 6 - len(player.inventory.items)):
        itemNames.append(".........")

    for i in range(0, len(itemNames)):

        if canAct:
            charStats += "^" + "─"*math.floor(len(itemNames[i])/2) + f"[{i + 1}]" + "─"*math.ceil(len(itemNames[i])/2-1)
        else:
            charStats += "^──" + "─"*len(itemNames[i])




    charStats += "╷ \n| "

        #lägger till item namen till string var
    for i in range(0, len(itemNames)):
        charStats += itemNames[i] + " | "
        
    charStats += "\n"
        #lägger till ett till långt sträck till stringen

    for i in range(0, len(itemNames)):
        charStats += "╵──" + "─"*(len(itemNames[i]))
    charStats += "╵"
    return charStats
        

player = Player()
Item("Wooden sword", 2, 0, 2, False, "weapon", [], []).ItemPickup()

Enter(difficultyIndex)
