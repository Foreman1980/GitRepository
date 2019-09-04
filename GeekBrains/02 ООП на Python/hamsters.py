from random import randint

class Hamster:
    health = 1
    position = [0, 0]

    def __init__(self, id, map):
        self.id = id
        self.health = randint(1, 4)
        self.position = self.getClearPosition(map)

    def onShot(self, strength):
        self.health -= strength
        return self.health > 0

    def damage(self):
        return randint(1, self.health)

    def getClearPosition(self, map):
        mapWidth = len(map.split('\n')[0])
        mapHeight = len(map.split('\n'))
        coords = [randint(0, mapWidth - 1), randint(0, mapHeight - 1)]
        while map.split('\n')[coords[1]][coords[0]] != '*':
            coords = [randint(0, mapWidth - 1), randint(0, mapHeight - 1)]
        return coords