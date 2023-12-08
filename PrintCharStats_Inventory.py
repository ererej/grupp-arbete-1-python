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


doorDescriptions = [[colored("Instead of having a regular doorhandle, the door has a lighter instead.", "red"), colored("The door seems to be slowly vanishing, like the way wood dissapears when it's burning", "red"), colored("The third door seems to be made out of coal.", "red")], 
[colored("A large icicle is hanging from the doorknob of this door.", "light_cyan"), colored("The door has the shape of a snowflake.", "light_cyan"), colored("This door seems to be made entirely of ice.", "light_cyan")], 
[colored("The door handle seems to have been crudely replaced with a dagger, don't touch the sharp end.", "dark_grey"), colored("The door seems to have the shape of a shield flipped upside-down.", "dark_grey"), colored("The door seems to have been made out weapons that were hastely melted down, since you can still tell the door was made out of weapon metal.", "dark_grey")], 
[colored("The first door has a ruler as a doorhandle.", "yellow"), colored("Behind the second door you hear the faint buzzing of a projector.", "yellow"), colored("The materials used to make this door seems to have been the following: Pens, erasers and rulers.", "yellow")]]


    




class Player():
    def __init__(self):
        #innehåller all data om spelaren.
        self.level = 1
        self.exp = 0
        self.expRequirement = 4
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

        for weakness in player.elements[ELEMENT_WEAKNESS]:
            if weakness == self.elements[ELEMENT_ATTACK_TYPE][attackIndex]:
                damage *= 2

        for resistance in player.elements[ELEMENT_RESISTANCE]:
            if resistance == self.elements[ELEMENT_ATTACK_TYPE][attackIndex]:
                damage /= 2

        player.health -= math.floor(damage)

        print(colored("\nYou sustain " + str(math.floor(damage)) + " " + self.elements[ELEMENT_ATTACK_TYPE][attackIndex] + "-type damage.", "red") + "\nPress [any] to continue")
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
        
        if self.itemType == "rejuvenation":
            # gives the player HP
            player.health += self.power
            print(f"You restored {self.power} health!")

        if self.itemType == "resistance-giver":
            # gives the player ALL resistances in the "resistancePotEffects" list
            for i in range(0, len(self.resistancePotEffects)):
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
            if len(player.inventory.items) < 5:
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
                if len(player.inventory.items) == 5:
                    if int(key) <= len(player.inventory.items):
                        break
            except:
                pass
            
        if key == "q":
            return
        if len(player.inventory.items) == 5:

            while key not in ['1','2','3','4','5']:
                key = Input()
            self.items[int(key) - 1].ItemDrop()
            foundItem.ItemPickup() # kanske ska lägga till att den lägger till det nya itemet i samma slot 
            return
        foundItem.ItemPickup() 
        return
        
# element types: fire, frost, physical, psychic, poison

# items have 8 paramiters: name, strength, health, elements, consumable, itemType, power, boostTypes, item description (for inventory)

itemList = [
    [["fire resistance potion", 0, 0, [], True, "resistance-giver", 0, ["fire"], "A burning flower is suspended in the liquid within this vial, although its petals and stem do not seem charred.\nDrink to gain resistance against fire damage, halving all damage taken of this type."], 
     ["molten shield", 1, 3, [], False, "resistance-giver", 0, ["fire", "cold"], "Only the hilt of this shield is not set aflame. \nUse this shield to gain resistance against certain damage types, reducing their damage toward you."],
     ["Baal's blade of infernal power", 0.5, 0, ["fire", "physical"], False, "weapon", 1.7, [], "A blade made of equal parts cold iron, sharp as death, molten rock, and infernal rage. \nSwing this at opponents to deal great amounts of damage, increased against enemies susceptible to its damage types."]],
    
    [["spell scroll: 'Fierce Blizzard'", 1, 0, ["frost", "frost"], True, "weapon", 2, [], "On this scroll are neatly inscribed runes and instructions for casting the 'Fierce Blizzard' spell. \nRead the scroll to deal great amounts of damage, increased against enemies susceptible to its damage type."], 
     ["pendant of winter's vitality", 0, 7, ["frost"], False, "rejuvenation", 3, [], "Possessing this pendant, an unbreakable ice crystal worn around the neck, fills you with courage. \nPray to Beira, god of winter and cold, to restore a small amount of health to yourself."],
     ["Braum's door-shield", 1, 5, [], False, "resistance-giver", 0, ["physical", "physical", "cold", "fire"], "Is this door a shield? Is this shield a door? Either way, it serves just as well for keeping death away.\nHold this door-shield between yourself and an enemy to halve all damage taken from them of certain types."]],

    [["regenerative potion", 0, 0, [], True, "rejuvenation", 4, [], "A small flask containing a blood-red liquid. \nDrink the contents to restore a small amount of health to yourself."],
     ["dark iron glaive", 1, 0, ["physical"], False, "weapon", 1.25, [], "A long, broad, jagged blade attached to a polearm. \nThrust or swing at opponents with this weapon to deal damage, increase against enemies susceptible to its damage types."], 
     ["quiver of poisoned arrows", 1, 0, ["poison"], False, "weapon", 1.4, [], "A quiver full of arrows. The tip of each one is covered in a mucus, toxic to the touch. \nFire this arrow at an opponent to deal great amounts of damage, increased against enemies suscetible to its damage types."],
     ["gauntlets of strength", 3, 1, ["physical"], False, "weapon", 0.8, [], "Putting on these glauntlets fills your entire body with an uverwhelming yet miniscule fraction of the otherworldly strength of Ares, the god of war. \nWith these, your punch becomes just as mean as your cut was, and you deal increased damage against enemies susceptible to its damage type."]],
    
    [["eraser", 0, 0, [], True, "rejuvenation", 4, [], "Its just a rubber/eraser. \nUse this item to erase some of your wounds, which somehow heals you."],
     ["sick diss track", 0, 0, ["psychic", "psychic"], False, "weapon", 1.2, [], "Wow this rap slaps hard, right bro?\nRap your enemies into battle. Pop some caps out there, man."],
     ["exam awnser sheet", 0, 0, ["answer", "answer", "answer", "psychic"], True, "weapon", 0.8, [], "A large stack of paper sheets that combined make up every answer to every test in every course in every year group in every country in all dimenttions. \nRead this to confuse most enemies, "]]]

#items have 8 paramiters: name, strength, health, elements, consumable, itemType, power, boostTypes, item description (for inventory)

# This dictionary contains all data on different monster types. They are sorted into different groups. Group 0: fire. Group 1: ice. Group 2: Knighs/weaponry. 3: lärare

# Tresures are on horizontal index 0
# Tresures have 3 paramiters: Name(idk why but why not (deleate it later if i dont need it)), enter_discription, exit_discription 

# traps are horizontal index 1
# traps have 2 paramiters: enterdisc, exitdisc

# Monster finns på horizontal index 2-4.
# monsterName, strength, health, elements: list[list[str]], enterDesc, attackMoveDesc, deathDesc

encounterList = [[["You enter the door and see a chest slowly sinking down in lava, you quickly save the chest and open it", "You close the chest and exit the room"], 
        ["As you enter a long corridor, you hear mechanical sounds coming from within the walls. The door locks behind you. Before you can react, you are ENVELOPED IN FIRE", "You sprint through the flames and exit this trapped room."], 
        ["fire slime", 2, 6, [["fire", "fire"], ["frost"], ["fire", "fire"]], "You step into a room covered in some sticky substance, most of which is AFLAME. \nA slimy creature stands before you, its body quickly incinerating even as it moves with struggling toward you.", ["The slime leaps onto your leg, putting your clothes on fire and forcing you to shake the thing off!", "Part of the slime is catapulted from its body, straight at your face!"], "What remains of the monster becomes plumes of smoke as it incinerates."], 
        ["dastardly imp", 6, 6, [["physical", "poison"], ["fire"], ["fire", "psychic"]], "A winged imp appears, although not at its full power; the skin around its head has been flayed off, and its wings are tattered.", ["The imp conjures fireballs from its hands and throws them at you!", "The imp lets out a terrible shriek, which tears through your mind!"], "The imp lets out a shreik of pain, clutching its wounds. Its wings become stale as it falls to the ground."], 
        ["dragon", 5, 17, [["psychic", "psychic"], ["physical"], ["fire", "physical"]], "As you enter, wind blows fast through the cavern you find yourself in. A dragon swoops down, in its claws clutching a lesser imp, which it proudly presents to you. A grin of sable-teeth spreads across its face. \n\n'Prepare yourself, lesser being!'", ["The Dragon unleashes a breath of fire upon you, like it's bathing you in a hundred suns!","The dragon slashes at your entire body at once, rending your flesh!"], "The dragon lets out a cry of pain... \n\n...it falls...\n\nto the ground...\n\n...its eyes...\n\n...vacant."]],
        
        [["Inside the room you see a item frozen in a block of ice, You brake the ice suronding it and!", "You quickly run out of the room to get away from the cold"], 
        ["The frigid gale of the north blows over you, FREEZING YOUR LIMBS!", "You run out of the room and when you do, the icicles stop falling and you see the massive pile of crushed ice that has formed."], 
        ["mad snowman", 3, 4, [["fire", "physical"], ["frost"], ["physical","frost"]], "A magical, wintery landscape is somehow enclosed under the dome you find yourself in as you enter the next room. \nA snowman standing in the middle of it attacks you!", ["The snowman throws a snowball at you! It doesn't hurt you, but then he drives a knife into your arm.", "The snowman throws a water baloon at you! Atleast you think it was water, but it turns out to be filled with liquid nitrogen!"], "The head of the snowman falls to the ground, and there is no more movement."], 
        ["snowstorm spirit", 5, 7, [[""], ["physical", "physical"], ["physical","frost"]], "POWERFUL WINDS immediately pull you through the door and into the room. A mass of gleaming energy floats in the center.", ["Another strong wind pulls you high into the air and then drives you STRAIGHT DOWN, slamming you into the ground!", "Water vapour in the air condenses into droplets, and then hardens into icicles that are all propelled toward you at fast speeds!"], "Chimes play throughout the room as the sprit implodes."], 
        ["glacier golem", 2, 30, [["frost", "frost"], [""], ["frost","physical"]], "The first thing that strikes you is the size of the thing. The second thing that strikes you is the glacier golem's giant fist.", ["The glacier golem renders itself immobile and cools down the room. You cannot escape; all exits are covered in ice. Your attacks are useless. You nearly freeze to death within the 3 hours that pass before heat returns and the golem reawakens.","The golem slams you with its giant arm!"], "The cold fire at the heart of the golem spills out as it slowly, with a soft thump, kneels down."]],
        
        [["In the middle of the room you see a chest of weapons you start looking through it.", "You leave the room and go on to the next adventure"], 
        ["The room you enter does not seem to have anything in it. But then the floor dissapears and you fall into a pit of spikes!", "You climb out of the pit and leave the room. A classic, but a dreadful trap."], 
        ["deserter", 3, 7, [["psychic", "frost", "poison"], [""], ["physical","fire"]], "A soldier lies in wait for you behin the door, but you manage to evade his first attack. He bears the banner of Mordor, but not much more on his tall, bare figure.", ["The soldier throws a knife at you, hitting you in the foot!", "The soldier slashes at you with his machete!"], "The solder lets out a groan, before falling to the ground motionless"],
        ["rider in the dark", 2, 25, [["frost"], ["psychic"], ["physical","psychic"]], "You enter a dimly-lit room. Standing infront of you seems to be a person riding a horse. You aren't to sure of its intentions, but best to attempt to kill it.", ["The rider attacks you with a spear! Or does it? It does not hurt that much...","The rider messes with your mind... in some unknown way. You are not entirely sure what he did, but you don't feel as healthy as before"], "The rider... disapears. It does not vanish, but at the same time it just... Well, it is dead, and you won, and that is what matters."], 
        ["thousand-pierced bear", 8, 16, [["frost", "fire", "fire"], ["physical", "physical", "poison"], ["phys", "phys"]], "You spot a bear infront of you! Judging by the various weapons stuck in its fur, it seems to be very dangerous!", ["The bear mauls you with its razor-sharp teeth!","The bear thrusts its claws into you like they were daggers!"], "The bear screams in great pain and tries to go for another attack, but falls to the ground dead before it could."]],
        
        [["You enter the door and find an empty classroom. You follow your natural instinct and start looting the teachers desk for useful items.", "You close the drawer and quickly run out of the classroom to not get caught red-handed."],
        ["Slowly, you enter the room. To your horror, you find on a whiteboard 100 meter wide, proof that you CANNOT REASONABLY still possess all the magical properties given to you in past rounds, proven with #FAXX and #Logic!", "'Can't argue with that', you think. You leave the room through a window, deeply appaled by this news."], 
        ["jesper engelmark", 3, 8, [["physical", "answer"], ["psychic"], ["physical","psychic"]], "You enter the room and suprise! It's Jesper Engelmark, and he has a murderous intent!", ["Jesper summons a door that he promtly slams in your face!","Jesper does an epic roast! You mind can't handle it properly!"], "Jesper dies and falls to the ground. Although on closer inspection, it might have been a clone. Oh well."], 
        ["annika westin", 6, 12, [["fire", "answer", "answer"], ["frost"], ["physical","psychic"]], "You enter the room. Suprise, it's Annika Westin!", ["Annika pulls out a pistol and shoots!","Annika pulls out a scroll and reads some magic! Your mind feels like it wants to go on vacation, away from this battle..."], "Annika falls to the ground and dies. It might have been a clone though, you are not sure."], 
        ["martin loman", 12, 24, [["fire", "answer"], ["psychic"], ["frost","psychic"]], "Wow! It's Martin Loman!", ["Martin did something!","Martin gave you a bad grade!"], "Martin dies."]]]


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
    MStats = []
    # Grabs stats for monster. Randomized monster level. Max ceil scales as percentage as player level increases. lvl 10 is max lvl as of writing.
    try:
        MStats : list = list(encounterList[element])[RND.randint(2, 2 + math.floor((player.level / 10) * (len(encounterList[element]) - 2)))]
    except:
        # If the player has not yet reached the level 2 monster, it will simply grab the lvl 1 monsters stats. This is because randint function does not accept two identical parameters.
        MStats: list = list(encounterList[element])[2]

    encounteredMonster = Monster(MStats[0], MStats[1], MStats[2], MStats[3], MStats[4], MStats[5], MStats[6])


    monsterStartHealth = encounteredMonster.health
    while (encounteredMonster.health > 0 and player.health > 0):
        os.system('cls')
        print(encounteredMonster.enterDesc + "\n"*2)

        if encounteredMonster.health == monsterStartHealth:
            print("press the index of an item in your inventory to use it and combat the sh*t out of that sorry sack of sob")
        else:
            print("The enemy has sustained a total of " + str(monsterStartHealth - encounteredMonster.health) + " damage.")
            print("press the index of an item in your inventory to use it and combat the sh*t out of that sorry sack of sob")

        print(PrintCharStats(True))
        key = Input()
        while key not in ['1','2','3','4','5'] or int(key) > len(player.inventory.items):
            if key == 'i' or key == "r":
                break
            key = Input()

            
        if key == "i":
            PrintInventory()
            continue
        elif key == "r":
            PrintHelpMenu()
            continue

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
    ItemStats: list = itemList[element][RND.randint( 0, math.ceil((player.level / 9) * len(itemList[element])) - 1)]
    foundItem = Item(ItemStats[0], ItemStats[1], ItemStats[2], ItemStats[3], ItemStats[4], ItemStats[5], ItemStats[6], ItemStats[7], ItemStats[8])
    player.inventory.PickUpItem(foundItem, element)

    os.system('cls')

    print(encounterList[element][0][1] + "\n"*2 + PrintCharStats(False) + "Press any key to continue!")
    Input()
    os.system('cls')




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
    os.system('cls')


def Main():
    
    global player

    player = Player()

    for i in player.inventory.items:
        player.inventory.items.remove(i)

    player.health = player.maxhealth
    Item("a wooden sword", 0, 0, ["physical"], False, "weapon", 0.7, [], "A flimsy sparring sword to swing at your opponents").ItemPickup()

    global hasWon
    hasWon = False
    while(not hasWon):
        os.system('cls')

        if player.health <= 0:

            print(colored("it would seem like you lost. Don't blame me. it's you who is total garbage.", "red") + colored("\n\n press [any] key to return to main menu!", "green"))
            Input()
            break
        
        if player.health > player.maxhealth:
            player.health = player.maxhealth



        screen1 = f"In the next room you see three doors"

        doorSet = [0, 0, 0]
        for i in range(1, len(doorSet) + 1):
            doorSet[i-1] = ( RND.randint(0,3) )
            screen1 += '\n'*2 + f"[{i}] " + doorDescriptions[ doorSet[i-1] ][i - 1]
 
        print(screen1 + "\n"*3 + PrintCharStats(False))
        
        key = ''
        while key not in ['1', '2', '3']:
            key = Input()
            
            if key == "r": 
                PrintHelpMenu()
        

            if key == "i":
                PrintInventory()
                
        
            os.system("cls")
            print(screen1 + "\n"*3 + PrintCharStats(False))
        
            encounterStyle = RND.randint(1, 10)

        if player.level <= 2:
            if encounterStyle <= 3:
                Treasure(doorSet[int(key) - 1])
            else: 
                Combat(doorSet[int(key) - 1])


        elif player.level <= 8:
            if encounterStyle <= 2:
                Trap(doorSet[int(key) - 1])
            elif encounterStyle <= 4:
                Treasure(doorSet[int(key) - 1])
            else:
                Combat(doorSet[int(key) - 1])

        else:
            Combat(doorSet[int(key) - 1])


        while player.exp >= player.expRequirement:
            os.system('cls')
            print("Congrats! You leveled up! You might make it here yet..." + "\n"*2 + colored("LEVEL +1\n", "green") + colored("STRENGTH +0.5", "yellow") + "\n"*2 + colored("You are filled with hope (heal 2)\n\n", "red"))
            player.exp -= player.expRequirement
            player.level += 1
            player.health += 2
            player.strength += 0.5
            player.expRequirement = math.floor(player.expRequirement * 1.3)

            if player.level == 10:
                print("Your path forks. The left path leads deeper into the dungeon. \nAt the end of a long tunnel, the right path ends in the vibrant sunlight of the outside. [l/r]")
                key = ""
                while key not in ['l', 'r']:
                    key = Input()

                if key == 'r':
                    print(colored("""
         )    )                     (        )  
     ( /( ( /(           (  (      )\ )  ( /(  
      )\()))\())     (    )\))(   '(()/(  )\()) 
     ((_)\((_)\      )\  ((_)()\ )  /(_))((_)\  
    __ ((_) ((_)  _ ((_) _(())\_)()(_))   _((_) 
    \ \ / // _ \ | | | | \ \((_)/ /|_ _| | \| | 
     \ V /| (_) || |_| |  \ \/\/ /  | |  | .` | 
      |_|  \___/  \___/    \_/\_/  |___| |_|\_|                       
                                                                                                    
                        """, "red"))
                    
                    hasWon = True
                    break

                



            print("The gods have blessed you! Your petty squabbles must be quite entertaining. A new path opens up before you, this one without a door. Inside, you can almost smell treasure...\n\nPress any key to collect it.")
            Input()
            Treasure(RND.randint(0, 3))
            

        
def PrintInventory():
    os.system("cls")
    for item in player.inventory.items:

        print(f"{item.name}: \n{item.descripion}" + "\n"*2 + f"Bonus strength: {item.strength} | Bonus health: {item.health}")

        if item.itemType == "weapon":
            printedText = "Item type: WEAPON | Damage types: "

            for element in item.elements:
                printedText += element + ", "
            
            printedText += str(item.power) + " power." 

        elif item.itemType == "rejuvenation":
            printedText = f"Item type: REJUVERATION | {item.power} power"

        elif item.itemType == "resistance-giver":
            printedText = "Item type: RESISTANCE-GIVER | Resistance types: "

            for resistance in item.resistancePotEffects:
                printedText += resistance + ", "

            
        print(printedText + "\n")
    
    print(PrintCharStats(False) + "\nPress anything to return")
    
    Input()

def PrintCharStats(canAct:bool):
    charStats = (colored("\nHealth: [" + '■'*(player.health) + ' '*(player.maxhealth-player.health) + "] ", "red") + colored(f"Strength: {player.strength} ", "yellow") + colored(f"Level: {roman.toRoman(player.level)} ({player.exp}/{player.expRequirement})", "green") + "\n")
    itemNames = []

    for i in range(0, len(player.inventory.items)):
        itemNames.append((player.inventory.items[i]).name)
    for i in range (0, 5 - len(player.inventory.items)):
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