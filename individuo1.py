from random import random


class Individuo:
	def __init__(self, cromossomo=None):
		self.tamanho = 9
		self.cromossomo = self.geraCromossomo() if not cromossomo else cromossomo
		self.fitness = None

	def geraCromossomo(self):
		self.cromossomo = []
		for _ in range(self.tamanho):
			if random() < 0.5:
				self.cromossomo.append(0)
			else:
				self.cromossomo.append(1)
		return self.cromossomo

	def __repr__(self):
		return f'Cromossomo: {self.cromossomo}, Fitness: {self.fitness}\n'

	def copia(self):
		indv_temp = Individuo(self.cromossomo)
		indv_temp.fitness = self.fitness
		return indv_temp

