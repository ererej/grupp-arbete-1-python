import random as RND

class Player():
    def __init__(self, name):
        pass

class Monster():
    def __init__(self, name) -> None:
        self.name = name

thisDict = {
    1: [Monster("Karl"), Monster(), 1, 2, 3],
    2: [Monster(), Monster()],
    3: [Monster("Pappersflygplansmonstret")],
    4: 123
}

someClassList: list[Monster] = thisDict[1]

someClass = someClassList[RND.randint(1, )]

player1 = Player()