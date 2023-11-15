import os
from enum import Enum

#class PlayerInventory:
    

#class 



class GameplayDescription:
    def __init__(self):
        print("\n Welcome to Farts and Boogies, your new favourite RPG game...")
        self.currentText = ""

    def NewDescription():
        os.system('cls')



class command(Enum):
    CLOSE_COMMAND = "c"
    IDLE = "e"


# -----------------------------------------------------------------------------------------------

LatestComm = command.IDLE
def MAIN_LOOP():
    LatestComm = command.IDLE
    while (LatestComm != command.CLOSE_COMMAND):
        while ((LatestComm in command._value2member_map_) == False):
            LatestComm = input("  INPUT ------>>>  ")

        

# -----------------------------------------------------------------------------------------------


"""
- Game name error
- Description (Area / Monster / whatev)
- 



"""

###

MAIN_LOOP()