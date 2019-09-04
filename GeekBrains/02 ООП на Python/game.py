from player import Player
from hamsters import Hamster

class Game:
    map = '****\n****\n****\n****'
    hamstersCount = len(map.split('\n'))

    def movePlayer(self, direction):
        if direction == 'w' and self.player.position[1] > 0:
            self.player.position[1] -= 1
        elif direction == 's' and self.player.position[1] < len(self.map.split('\n')) - 1:
            self.player.position[1] += 1
        elif direction == 'a' and self.player.position[0] > 0:
            self.player.position[0] -= 1
        elif direction == 'd' and self.player.position[0] < len(self.map.split('\n')[0]) - 1:
            self.player.position[0] += 1
        elif direction == 'q':
            self.gameOn = False
            #exit()
        self.onMove(direction)

    destination = {'a': 'd', 'd': 'a', 'w': 's', 's': 'w'}

    def onMove(self, direction):
        for h in self.hamsters:
            if h.position == self.player.position:
                playerDamage = self.player.damage()
                hamsterDamage = h.damage()
                if h.onShot(playerDamage):
                    self.movePlayer(self.destination[direction])
                    self.player.health -= hamsterDamage
                    print(f'Сила удара игрока {playerDamage}. У хомяка № {h.id} осталось {h.health} ед. здоровья.')
                    if self.player.health > 0:
                        print(f'Игрок получил ответный урон в {hamsterDamage} ед. Текущее здоровье игрока {self.player.health}')
                    else:
                        print('Поражение...Игрок убит ответным уроном в {hamsterDamage} ед.')
                        self.gameOn = False
                        #exit()
                else:
                    del self.hamsters[self.hamsters.index(h)]
                    self.player.health -= hamsterDamage
                    print(f'Сила удара игрока {playerDamage}. Хомяк № {h.id} был убит')
                    if self.player.health > 0:
                        print(f'Игрок получил ответный урон в {hamsterDamage} ед. Текущее здоровье игрока {self.player.health}')
                    elif len(self.hamsters) > 0:
                        print('Поражение...Игрок убит.')
                        self.gameOn = False
                        #exit()
                    else:
                        print(f'Игрок убит ответным уроном в {hamsterDamage} ед. Убиты все, никто не победил.')
                        self.gameOn = False
                        #exit()

    def addPoint(self, position, char, map):
        s = map.split('\n')
        s[position[1]] = s[position[1]][:position[0]] + f'{char}' + s[position[1]][position[0] + 1:]
        return '\n'.join(s)

    def getFullMap(self):
        map = self.map
        map = self.addPoint(self.player.position, 'x', map)
        for h in self.hamsters:
#            if h.health > 0:
            map = self.addPoint(h.position, h.id, map)
        return map

    def renderMap(self):
        print(self.getFullMap())

    def __init__(self):
        gameOn = True
        self.player = Player(self.map)
        self.hamsters = []
        for i in range(self.hamstersCount):
            self.hamsters.append(Hamster(f'{i+1}', self.getFullMap()))

    def start(self):
        self.renderMap()
        while self.gameOn:
            command = input('Введите команду: ')
            if command in ['w', 'a', 's', 'd', 'q']:
                self.movePlayer(command)
            elif command == 'e':
                self.player.rest()
            self.renderMap()
            if len(self.hamsters) == 0:
                self.gameOn = False
                print('Победа!')

game = Game()
game.start()