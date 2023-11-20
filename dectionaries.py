import random as RND
import math

difficultyMultiplier = 1

#| Jag tror det är en bra idé att lägga monsters hp på ~10 och player hp på ~25. 
#| Med större nummer fungerar difficulty scaling och randomized damage bättre och tal blir mer förenliga.
#| Varje difficulty level är en increment på 30% stats.
#| 

class Player():
    def __init__(self, name):
        pass

class Monster():
    def __init__(self, name, strength, health, threatTypes, attackMoveDesc, deathDesc) -> None:

        self.name = name
        self.strength = math.ceil(strength * difficultyMultiplier)
        self.health = math.ceil(health * difficultyMultiplier)
        self.threatType: list[str] = threatTypes
        
        self.attackMoveDesc = attackMoveDesc
        self.deathDesc = deathDesc



    def CombatRound(playerResistances):
        pass


MonsterDict = {
    1: [Monster("Karl", 4, 8, ["Mattenörd", "Papper"], """

Karl kastar sin matteperm mot dig, och den träffar dig RÄTT I SKREVET! *critical strike* *oof*

                """, """
                
Mattenörden Karl dog av din attack, och hans matteblod flödar ur såren. Han dör ledsen. Han tog alldrig reda på svaret på livets gåta -- 
                hur man räknar ut arean under en funktions graf...
                
                """), Monster("Jesper", 6, 10, "Fysiklärare", """

Jesper stänger dörren rätt i ditt ansikte!

""", """



"""), 1, 2, 3],
    2: [Monster(), Monster()],
    3: [Monster("Pappersflygplansmonstret")],
    4: 123
}

someClassList: list[Monster] = MonsterDict[1]

someClass = someClassList[RND.randint(1, )]

player1 = Player()