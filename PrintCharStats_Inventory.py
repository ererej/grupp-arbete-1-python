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

ELEMENT_WEAKNESS = 0
ELEMENT_RESISTANCE = 1
ELEMENT_ATTACK_TYPE = 2


doorDescriptions = [[colored(" Instead of having a regular doorhandle, the door has a lighter instead.", "red"), colored(" The door seems to be slowly vanishing, like the way wood dissapears when it's burning", "red"), colored(" The third door seems to be made out of coal.", "red")], 
[colored(" A large icicle is hanging from the doorknob of this door.", "light_cyan"), colored(" The door has the shape of a snowflake.", "light_cyan"), colored(" This door seems to be made entirely of ice.", "light_cyan")], 
[colored(" The door handle seems to have been crudely replaced with a dagger, don't touch the sharp end.", "dark_grey"), colored(" The door seems to have the shape of a shield flipped upside-down.", "dark_grey"), colored(" The door seems to have been made out weapons that were hastely melted down, since you can still tell the door was made out of weapon metal.", "dark_grey")], 
[colored(" The first door has a ruler as a doorhandle.", "yellow"), colored(" Behind the second door you hear the faint buzzing of a projector.", "yellow"), colored(" The materials used to make this door seems to have been the following: Pens, erasers and rulers.", "yellow")]]


    




class Player():
    def __init__(self):
        #innehåller all data om spelaren.
        self.level = 1
        self.exp = 0
        self.expRequirement = 3
        self.maxhealth = 10
        self.health = 10
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

    def CombatActive(self):
        try:
            attackIndex = RND.randint(0, len(self.attackMoveDesc) - 1)
        except:
            attackIndex = 0

        print(self.attackMoveDesc[attackIndex])

        damage = self.strength

        for i in player.elements[ELEMENT_WEAKNESS]:
            if player.elements[ELEMENT_WEAKNESS][i] == self.elements[ELEMENT_ATTACK_TYPE][attackIndex]:
                damage *= 2

        for i in player.elements[ELEMENT_RESISTANCE]:
            if player.elements[ELEMENT_RESISTANCE][i] == self.elements[ELEMENT_ATTACK_TYPE][attackIndex]:
                damage /= 2

        player.health -= math.floor(damage)

        print(colored("\nYou sustain " + str(damage) + " " + self.elements[ELEMENT_ATTACK_TYPE][attackIndex] + "-type damage.", "red") + "\nPress [any] to continue")
        Input()


    

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
    def __init__(self, name, strength, health, elements, consumable: bool, itemType, power, resistancePotEffects: list, description):

        self.name = name
        self.descripion = description

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

        print("You used " + self.name + "!\n")

        # Weapons deal (player strength * damageMultiplier) damage of the item's type. Monsters can 
        if self.itemType == "weapon":
            # 
            damage = float(player.strength)

            for i in range(0, len(monster.elements[ELEMENT_WEAKNESS]) - 1):
                if monster.elements[ELEMENT_WEAKNESS][i] in self.elements:
                    damage *= 2

            for i in range(0, len(monster.elements[ELEMENT_RESISTANCE]) - 1):
                if monster.elements[ELEMENT_RESISTANCE][i] in self.elements:
                    damage /= 2
            
            monster.health -= math.floor(damage * self.power)
            print("Your opponent sustained " + str(math.floor(damage * self.power)) + " damage!")
        
        if self.itemType == "rejuveration":
            # gives the player HP
            player.health += self.power
            print(f"You restored {self.power} health!")

        if self.itemType == "resistance-giver":
            # gives the player ALL resistances in the "resistancePotEffects" list
            for i in self.resistancePotEffects:
                player.elements[ELEMENT_RESISTANCE].append(self.resistancePotEffects[i])
            print("You gained some magical resistances!")

        if self.consumable == True:
            self.ItemDrop()




class Inventory():
    def __init__(self):
        self.items: list[Item] = []


    
    def PickUpItem(self, foundItem:Item, element):

        while True:
            os.system("cls")
            global canAct
            canAct = True
            print(colored(encounterList[element][0][0]))
            print(f"\nYou found " + colored(f"{foundItem.name}", "green") + ", a", colored(f"{foundItem.itemType}", "red") + "-type item")
            if len(player.inventory.items) < 6:
                print(f"\n[E] Add the item to your inventory")
            else:
                print("\nPress the index of an item in your inventory to replace it with the new item")
            print("\n[Q] discard the item and move on")
            print("\n[I] to open inventory")
            print("\n"*2 + PrintCharStats(True))
            key = Input()
            #väntar på en valid input
            if key == "q" or key == "e":
                break
            elif key == "i":
                PrintInventory()
            elif key == "r":
                PrintHelpMenu()
            try:
                if len(player.inventory.items) == 6:
                    if int(key) <= len(player.inventory.items):
                        break
            finally:
                pass
            
        if key == "q":
            return
        if len(player.inventory.items) == 6:

            self.items[int(key) - 1].ItemDrop()
            foundItem.ItemPickup() # kanske ska lägga till att den lägger till det nya itemet i samma slot 
            return
        foundItem.ItemPickup() 
        return
        
# element types: fire, frost, phys (physical), psy (psionic)
# name, strength, health, elements, consumable: bool, itemType, power, resistancePotEffects: list

# "true" item types: stat stick, weapon, healing potion, resistance potion
# weapons need name, strength, hp, [damage types], consumable: bool, itemType ("weapon"), power (damage multiplier), [nothing]

itemList = [
    [["a fire resistance potion", 0, 0, [], True, "resistance-giver", 0, ["fire"], "A burning flower is suspended in "], 
     ["the blade of infinite infernal power", 2, 2, ["fire", "physical"], False, "weapon", 2.5, [], ""]],
    [["a scroll of frostbite", 1, 0, ["frost"], True, "weapon", 3, [], ""], 
     ["a pendant of winter's vitality", 0.5, 7, ["frost"], False, "rejuveration", 2, [], ""]],
    [["a wooden sword", 0.5, 0, ["physical"], False, "weapon", 0.75, [], ""], 
     ["the gauntlets of strength", 3, 1, ["physical"], False, "weapon", 0.5, [], ""]],
    [["Exam awnser key", 2, 1, 3, True, "weapon", [], [], ""], 
     ["teacher item place holder", 2, 1, 3, False, "weapon", [], [], ""]]]

#items have 8 paramiters: name, strength, health, elements, consumable, itemType, power, boostTypes, item description (for inventory)

# This dictionary contains all data on different monster types. They are sorted into different groups. Group 0: fire. Group 1: ice. Group 2: Knighs/weaponry. 3: lärare

# Tresures are on horizontal index 0
# Tresures have 3 paramiters: Name(idk why but why not (deleate it later if i dont need it)), enter_discription, exit_discription 

# traps are horizontal index 1
# traps have 2 paramiters: enterdisc, exitdisc

# Monster finns på horizontal index 2-4.
# monsterName, strength, health, elements: list[list[str]], enterDesc, attackMoveDesc, deathDesc

encounterList = [[["placeholder enter disc", "place holder exit disc"], #The lava pit 
        ["As you enter a long corridor, you hear mechanical sounds coming from within the walls. The door locks behind you. Before you can react, you are ENVELOPED IN FIRE", "You sprint through the flames and exit this trapped room."], 
        ["THE FIRE SLIME", 2, 6, [["frost"], ["fire"], ["fire", "fire"]], "A slimy, spherical creature that also appears to be on fire stands infront of you!", ["The slime jumps into you! Luckely its body does not hurt. The flames however, does.", "The slime spits out a stream of fire onto you!"], "The flames on the monster extinguish, and it solidifies."], 
        ["DASTARDLY IMP", 6, 8, [["physical"], ["fire"], ["fire","psychic"]], "An imp appears! It seems to be quite cruel with its attacks.", ["The imp throws fireballs at you!","The imp casts a spell upon you! It seems like it damaged your mind."], "The imp lets out a shreik, and dies."], 
        ["DRAGON"], 8, 25, [["psychic"], ["physical"], ["fire","physical"]], "You spot a formidable dragon standing some distance away. You try to avoid it, but it notices you. Prepare for battle!", ["The Dragon breathes fire at you!","The Dragon slashes its claws at you!"], "The dragon lets out a cry of pain, before falling to the ground dead."],
        [["placeholder enter disc", "place holder exit disc"], 
        ["The frigid gale of the north blows over you, FREEZING YOUR LIMBS!", "You run out of the room and when you do, the icicles stop falling and you see the massive pile of crushed ice that has formed."], 
        ["THE MAD SNOWMAN", 4, 4, [["fire"], ["frost"], ["physical","frost"]], "You notice a snowman in the room. When you go to get a closer look, it wakes to life!", ["The snowman throws a snowball at you! It doesn't hurt you, but then he drives a knife into your arm.", "The snow man throws a water baloon at you! Atleast you think it was water, but it turns out to be filled with liquid nitrogen!"], "The head of the snowman falls to the ground, and there is no more movement."], 
        ["THE FROZEN SPIRIT", 5, 15, [["psychic"], ["physical"], ["psychic","frost"]], "You enter a room, but it is empty. Then a spirit flies in through the wall!", ["The spirit casts a spell, draining your sanity and mental health.","The spirit causes the vapor in the air to freeze into icicles, then it throws them at you!"], "The sprits vanishes into thin air."], 
        ["THE GLACIER GOLEM"], 14, 8, [["physical"], ["psychic"], ["frost","physical"]], "A gargantuan ice golem stands infront of you!", ["The golem cools the area significantly to the point you develop frostbite!","The golem slams you with its giant arm!"], "Cracks appear on the golem moments before it falls apart. Turns out being made of ice made it quite fragile."],
        [["placeholder enter disc", "place holder exit disc"], 
        ["The room you enter does not seem to have anything in it. But then the floor dissapears and you fall into a pit of spikes!", "You climb out of the pit and leave the room. A classic, but a dreadful trap."], 
        ["THE DESERTER", 3, 7, [["psychic"], ["physical"], ["physical","fire"]], "You spot a soldier infront of you! He seems to have deserted the army he once belonged to.", ["The soldier tries to shoot you with his rifle, but it's jammed. So then he attacks you with it like a club!","The soldier attacks you with a miniature flamethrower!"], "The solder lets out a groan, before falling to the ground motionless"],
        ["THE RIDER IN THE DARK", 2, 25, [["frost"], ["psychic"], ["physical","psychic"]], "You enter a dimly-lit room. Standing infront of you seems to be a person riding a horse. You aren't to sure of its intentions, but best to attempt to kill it.", ["The rider attacks you with a spear! Or does it? It does not hurt that much...","The rider messes with your mind... in some unknown way. You are not entirely sure what he did, but you don't feel as healthy as before"], "The rider... disapears. It does not vanish, but at the same time it just... Well, it is dead, and you won, and that is what matters."], 
        ["THE THOUSAND-PIERCED BEAR", 10, 35, [["frost"], ["physical"], ["phys, phys"]], "You spot a bear infront of you! Judging by the various weapons stuck in its fur, it seems to be very dangerous!", ["The bear mauls you with its razor-sharp teeth!","The bear thrusts its claws into you like they were daggers!"], "The bear screams in great pain and tries to go for another attack, but falls to the ground dead before it could."]],
        [["You enter the door and find an empty classroom. You follow your natural instinct and start looting the teachers desk for useful items.", "You close the drawer and quickly run out of the classroom to not get caught red-handed."],
        ["Slowly, you enter the room. To your horror, you find on a whiteboard 100 meter wide, proof that you CANNOT REASONABLY still possess all the magical properties given to you in past rounds, proven with #FAXX and #Logic!", "'Can't argue with that', you think. You leave the room through a window, deeply appaled by this news."], 
        ["JESPER ENGELMARK", 3, 8, [["physical"], ["psychic"], ["physical","psychic"]], "You enter the room and suprise! It's Jesper Engelmark, and he has a murderous intent!", ["Jesper summons a door that he promtly slams in your face!","Jesper does an epic roast! You mind can't handle it properly!"], "Jesper dies and falls to the ground. Although on closer inspection, it might have been a clone. Oh well."], 
        ["ANNIKA WESTIN", 6, 12, [["fire"], ["frost"], ["physical","psychic"]], "You enter the room. Suprise, it's Annika Westin!", ["Annika pulls out a pistol and shoots!","Annika pulls out a scroll and reads some magic! Your mind feels like it wants to go on vacation, away from this battle..."], "Annika falls to the ground and dies. It might have been a clone though, you are not sure."], 
        ["MARTIN LOMAN", 12, 24, [["fire"], ["psychic"], ["frost","psychic"]], "vi skriver lite text här", ["",""], ""]]] # ADD DESCS HERE


def Input():
    keyboard.read_key()

    returnedKey = keyboard.read_key()

    return returnedKey.lower()

def PrintHelpMenu():
    os.system('cls')
    print("\n\nHow to play: \n   1: Use items strategically to defeat monsters etcetcetc \n   2: eznella plz do not hold keys plzzz \n\nKeybinds:\n   [R]: Brings up this menu \n   [I]: Opens the inventory\n   [1/2/3]: Enter a room through chosen door\n\nPress any key to return to where you where!")
    Input()

difficultyMap = [[1, colored("nuuuuub", "green")], [1.2, colored("normal", "yellow")], [1.4, colored("martin going godmode", "red")]]
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

    # Grabs stats for monster. Randomized monster level. Max ceil scales as percentage as player level increases. lvl 10 is max lvl as of writing.
    try:
        MStats : list = list(encounterList[element])[RND.randint(2, math.floor((player.level / 10) * (len(encounterList[element]) - 2)))]
    except:
        # If the player has not yet reached the level 2 monster, it will simply grab the lvl 1 monsters stats. This is because randint function does not accept two identical parameters.
        MStats: list = list(encounterList[element])[2]

    encounteredMonster = Monster(MStats[0], MStats[1], MStats[2], MStats[3], MStats[4], MStats[5], MStats[6])


    monsterStartHealth = encounteredMonster.health
    while (encounteredMonster.health > 0 and player.health > 0):
        os.system('cls')
        print(encounteredMonster.enterDesc + "\n"*2)

        if encounteredMonster.health == monsterStartHealth:
            print("Use an item in your inventory to combat the sh*t out of that sorry sack of sob")
        else:
            print("The enemy has sustained a total of " + str(monsterStartHealth - encounteredMonster.health) + " damage.")

        print(PrintCharStats(True))
        key = Input()
        while key not in ['1','2','3','4','5','6'] or int(key) > len(player.inventory.items):
            key = Input()
        
        usedItem = player.inventory.items[int(key) - 1]
        usedItem.CombatActive(encounteredMonster)


        if encounteredMonster.health > 0:
            encounteredMonster.CombatActive()

    if player.health > 0:

        player.exp += encounteredMonster.strength

        print(encounteredMonster.name + " has fallen, and you emerge victorious..." + "\n"*2 + "...For now.\n")


    print("\nPress any key to continue")

    Input()


def Treasure(element):
    os.system("cls")
    ItemStats: list = list(itemList[element])[RND.randint(0, len(itemList[element])-1)]
    foundItem = Item(ItemStats[0], ItemStats[1], ItemStats[2], ItemStats[3], ItemStats[4], ItemStats[5], ItemStats[6], ItemStats[7], ItemStats[8])
    player.inventory.PickUpItem(foundItem, element)

    print(encounterList[element][0][1] + "\n"*2 + PrintCharStats(False) + "Press any key to continue!")
    Input()




def Trap(element):
    os.system('cls')
    print(encounterList[element][1][0])

    if element == 3:
        player.elements[1] = []

        print("\n"*2 + "Your magical resistances have all been removed.")

    if element == 1:
        print("\n"*2 + "You feel some of your strength leave you.")
        player.strength -= 0.5

    if element == 0:
        if len(player.inventory.items) > 1:
            killedItem = player.inventory.items[RND.randint(0, len(player.inventory.items) - 1)]
            print("\n"*2 + killedItem.name + " in your inventory has been destroyed.")
            killedItem.ItemDrop()

    damageTaken = RND.randint(1, 2)
    player.health -= damageTaken
    print("\nYou took "+ colored(f"{damageTaken} damage!", "red") + "\n")
    player.exp += math.ceil(player.expRequirement / 4)
    print(encounterList[element][1][1])
    print("\nPress any key to continue!")
    Input()


def Main():
    
    global player

    player = Player()

    for i in player.inventory.items:
        player.inventory.items.remove(i)

    player.health = player.maxhealth
    Item("a wooden sword", 0.5, 0, ["physical"], False, "weapon", 0.7, [], "A sparring sword to swing at your opponents").ItemPickup()

    while(True):
        os.system('cls')

        if player.health <= 0:

            print("it would seem you lost. Dont blame me. its you whos total garbage. Wanna play again?")
            Input()
            break
        
        if player.health > player.maxhealth:
            player.health = player.maxhealth

        while player.exp >= player.expRequirement:

            print("Congrats! You leveled up! You might make it here yet..." + "\n"*2 + "LEVEL +1\nSTRENGTH +0.5" + "\n"*2 + "You are filled with hope (heal 2)\n")
            player.exp -= player.expRequirement
            player.level += 1
            player.health += 2
            player.strength += 0.5
            player.expRequirement = math.floor(player.expRequirement * 1.3)


        screen1 = f"In the next room you see three doors"

        doorSet = [0, 0, 0]
        for i in range(1, len(doorSet) + 1):
            doorSet[i-1] = ( RND.randint(0,3) )
            screen1 += '\n'*2 + f"[{i}]" + list( doorDescriptions[ doorSet[i-1] ] )[i - 1]
 
        print(screen1 + "\n"*3 + PrintCharStats(False))
        
        key = ''
        while key not in ["i", 'r', '1', '2', '3']:
            key = Input()

        if key == "r": 
            PrintHelpMenu()

        if key == "i":
            PrintInventory()

        if key in ['1', '2', '3']:
            
            encounterStyle = RND.randint(1, 10)

            if player.level <= 2:
                if encounterStyle <= 3:
                    Treasure(doorSet[int(key) - 1])
                else: 
                    Combat(doorSet[int(key) - 1])


            elif player.level <= 8:
                if encounterStyle <= 2:
                    Trap(doorSet[int(key) - 1])
                elif encounterStyle <= 5:
                    Treasure(doorSet[int(key) - 1])
                else:
                    Combat(doorSet[int(key) - 1])

            else:
                Combat(doorSet[int(key) - 1])
            

        
def PrintInventory():
    os.system("cls")
    for item in player.inventory.items:

        print(f"{item.name}: \n{item.descripion}" + "\n"*2 + f"Bonus strength: {item.strength} | Bonus health: {item.health}")

        if item.itemType == "weapon":
            printedText = "Item type: WEAPON | Damage types: "

            for element in item.elements:
                printedText += element + ", "
            
            printedText += str(item.power) + " power." 

        elif item.itemType == "rejuveration":
            printedText = f"Item type: REJUVERATION | {item.power} power"

        elif item.itemType == "resistance-giver":
            printedText = "Item type: RESISTANCE-GIVER | Resistance types: "

            for resistance in item.resistancePotEffects:
                printedText += resistance + ", "

            
        print(printedText)
    
    print(PrintCharStats(False) + "\nPress [Q] to return")
    
    while keyboard.read_key() != 'q':
        pass

def PrintCharStats(canAct:bool):
    charStats = (colored("\nHealth: [" + '■'*(player.health) + ' '*(player.maxhealth-player.health) + "] ", "red") + colored(f"Strength: {player.strength} ", "yellow") + colored(f"Level: {roman.toRoman(player.level)} ", "green") + "\n")
    itemNames = []

    for i in range(0, len(player.inventory.items)):
        itemNames.append((player.inventory.items[i]).name)
    for i in range (0, 6 - len(player.inventory.items)):
        itemNames.append(".........")

    for i in range(0, len(itemNames)):

        if canAct:
            charStats += "╷" + "─"*math.floor(len(itemNames[i])/2) + f"[{i + 1}]" + "─"*math.ceil(len(itemNames[i])/2-1)
        else:
            charStats += "╷──" + "─"*len(itemNames[i])




    charStats += "╷ \n| "

        #lägger till item namen till string var
    for i in range(0, len(itemNames)):
        charStats += itemNames[i] + " | "
        
    charStats += "\n"
        #lägger till ett till långt sträck till stringen

    for i in range(0, len(itemNames)):
        charStats += "╵──" + "─"*(len(itemNames[i]))
    charStats += "╵\n"
    return charStats
        

player = Player()

Enter(difficultyIndex)

# DET FINNS INGET VAPEN I INVENTORY VID SPELETS START JUST NU MAN KAN EJ ANFALLA JUST NU
# Notes: Öka antalet health spelaren börjar med, det är för lite ||| Förlorar man spelet behöver man starta upp koden igen ||| the blade of infinite infernal power är: 1. OP 2. typ ett måste för att vinna just nu p.g.a balancing |||
# Rapporterar buggar till folk som kan koden bättre: Jonas
#1. Försöker använda "teacher item placeholder"
# Traceback (most recent call last):
# File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 513, in <module>
#    Enter(difficultyIndex)
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 310, in Enter   
#    Main()
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 450, in Main    
#    Combat(doorSet[int(key) - 1])
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 342, in Combat  
#    usedItem.CombatActive(encounteredMonster)
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 146, in CombatActive
#    monster.health -= math.floor(damage * self.power)
#                                 ~~~~~~~^~~~~~~~~~~~
#TypeError: can't multiply sequence by non-int of type 'float'
#2. Försökte gå in i rum 1
#In the next room you see three doors

#[1] Instead of having a regular doorhandle, the door has a lighter instead.

#[2] Behind the second door you hear the faint buzzing of a projector.

#[3] The materials used to make this door seems to have been the following: Pens, erasers and rulers.


#Health: [■■■■■■■■■■■■■■■■■■■■] Strength: 11.5 Level: VIII 
#╷────────────────╷──────────────────────────────────────╷─────────────────╷────────────────────────────────╷───────────╷───────────╷ 
#| a wooden sword | the blade of infinite infernal power | Exam awnser key | a pendant of winter's vitality | ......... | ......... | 
#╵────────────────╵──────────────────────────────────────╵─────────────────╵────────────────────────────────╵───────────╵───────────╵ 

#Traceback (most recent call last):
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 513, in <module>
#    Enter(difficultyIndex)
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 310, in Enter   
#    Main()
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 459, in Main    
#    Combat(doorSet[int(key) - 1])
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 323, in Combat
#    encounteredMonster = Monster(MStats[0], MStats[1], MStats[2], MStats[3], MStats[4], MStats[5], MStats[6])
#                                 ~~~~~~^^^
#TypeError: 'int' object is not subscriptable
#3. försökte trycka på q och inte plocka upp föremål
#placeholder enter disc

#You found a pendant of winter's vitality, a rejuveration-type item

#Press the index of an item in your inventory to replace it with the new item

#[Q] discard the item and move on

#[I] to open inventory


#Health: [■■■■■■■■■■■■■■■■■■  ] Strength: 11.5 Level: VI 
#╷───────[1]──────╷──────────────────[2]─────────────────╷──────────[3]──────────╷───────────────[4]──────────────╷───────[5]──────╷────────────[6]────────────╷

#| a wooden sword | the blade of infinite infernal power | a scroll of frostbite | a pendant of winter's vitality | a wooden sword | teacher item place holder |

#╵────────────────╵──────────────────────────────────────╵───────────────────────╵────────────────────────────────╵────────────────╵───────────────────────────╵

#Traceback (most recent call last):

#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 513, in <module>
#    Enter(difficultyIndex)
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 310, in Enter
#    Main()
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 457, in Main
#    Treasure(doorSet[int(key) - 1])
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 364, in Treasure
#    player.inventory.PickUpItem(foundItem, element)
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 206, in PickUpItem
#    self.items[int(key) - 1].ItemDrop()
#              ^^^^^^^^
#ValueError: invalid literal for int() with base 10: 'q'
# 4. man plockar alltid upp föremål, även om man trycker på q
# 5. försökte gå in i rum 3
#Congrats! You leveled up! You might make it here yet...

#In the next room you see three doors

#[1] The door handle seems to have been crudely replaced with a dagger, don't touch the sharp end.

#[2] The door has the shape of a snowflake.

#[3] The third door seems to be made out of coal.


#╷────────────────╷──────────────────────────────────────╷───────────────────────╷────────────────────────────────╷────────────────────────────────╷───────────╷

#| a wooden sword | the blade of infinite infernal power | a scroll of frostbite | a pendant of winter's vitality | a pendant of winter's vitality | ......... |

#╵────────────────╵──────────────────────────────────────╵───────────────────────╵────────────────────────────────╵────────────────────────────────╵───────────╵

#Traceback (most recent call last):
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 513, in <module>
#    Enter(difficultyIndex)
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 310, in Enter
#    Main()
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 459, in Main
#    Combat(doorSet[int(key) - 1])
#  File "c:\Pythonprogramm\grupp-arbete-1-python\PrintCharStats_Inventory.py", line 323, in Combat
#    encounteredMonster = Monster(MStats[0], MStats[1], MStats[2], MStats[3], MStats[4], MStats[5], MStats[6])
#                                            ~~~~~~^^^
#IndexError: list index out of range
#