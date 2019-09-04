from random import randint

class Player:
	health = 10
	maxHealth = 10
	position = [0, 0]

	def __init__(self, map):
		mapWidth = len(map.split('\n')[0])
		mapHeight = len(map.split('\n'))
		self.position = [randint(0, mapWidth-1), randint(0, mapHeight-1)]

	def rest(self):
		if self.health < self.maxHealth:
			self.health += 1
			print(f'Игрок восстановил 1 ед. здоровья, текущее значение {self.health}')
		else:
			print('У игрока максимальный уровень здоровья')

	def damage(self):
		return randint(1, 4)