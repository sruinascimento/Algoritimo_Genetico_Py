from produto1 import Produto 
from individuo1 import Individuo 
from random import sample, randint, random


class Ambiente:
	def __init__(self):
		self.tamanho_populacao = 10
		self.melhor_individuo = None
		self.taxa_crossing_over = 0.9
		self.taxa_mutacao = 0.02
		self.populacao_parada = 50

	def start(self):
		populacao = self.geraPopulacaoInicial()
		self.avalia(populacao)
		for _ in range(self.populacao_parada):
			populacao = self.reproducao(populacao)
			self.avalia(populacao)
		return self.melhor_individuo

	def start1(self):
		populacao = self.geraPopulacaoInicial()
		self.avalia(populacao)
		selecionados = self.seleciona(populacao)
		_2geracao = self.cruza(selecionados)
		self.avalia(_2geracao)
		print('<Populacao:>')
		print(populacao)
		print('<Selecionados:>')
		print(selecionados)
		print('<2a Geracao:>')
		print(_2geracao)
		print('<2a Geracao Mutada:>')
		self.muta(_2geracao)
		self.avalia(_2geracao)
		print(_2geracao)
		print('<Melhor Individuo:>')
		print(self.melhor_individuo)


	def geraProdutos(self):
		lista_produtos = []
		lista_produtos.append(Produto('Iphone X', 0.0000899, 2991.12))
		lista_produtos.append(Produto('TV 55', 0.400, 4346.99))
		lista_produtos.append(Produto('TV 50', 0.290, 3999.90))
		lista_produtos.append(Produto('TV 42', 0.200, 2999.00))
		lista_produtos.append(Produto('Notebook DELL', 0.00350, 2499.90))
		lista_produtos.append(Produto('Ventilador Panasonic', 0.496, 199.90))
		lista_produtos.append(Produto('Microondas Electrolux', 0.0424, 308.66))
		lista_produtos.append(Produto('Microondas LG', 0.0544, 429.90))
		lista_produtos.append(Produto('Microondas Panasonic', 0.0319, 299.29))
		return lista_produtos

	def geraPopulacaoInicial(self) -> list:
		populacao_temp = [Individuo() for _ in range(self.tamanho_populacao)]	
		self.melhor_individuo = populacao_temp[0]
		return populacao_temp

	def avalia(self, populacao:list) -> None:	
		for individuo in populacao:
			individuo.fitness = self.calculaFitness(individuo)
			self.melhorIndividuo(individuo)

	def calculaFitness(self, individuo) -> float:
		lista_produtos = self.geraProdutos()
		i = 0
		espaco_usado = 0
		valores = 0
		for value in individuo.cromossomo:
			if value == 1:
				espaco_usado += lista_produtos[i].espaco 
				valores += lista_produtos[i].valor
			i += 1		
		if espaco_usado <= 1.0: 
			return valores
		return 1.0

	def melhorIndividuo(self, individuo) -> None:
		if self.melhor_individuo.fitness < individuo.fitness:
			self.melhor_individuo = individuo.copia()
			return

	def seleciona(self, populacao:list) -> list:
		count = int(self.tamanho_populacao * self.taxa_crossing_over)
		piscina = []
		for _ in range(count):
			selecionados = sample(populacao, 3)
			selecionados.sort(key=lambda individuo: individuo.fitness)
			piscina.append(selecionados[-1])		
		return piscina

	def cruza(self, selecionados:list) -> list:
		count = int(self.tamanho_populacao * self.taxa_crossing_over)
		novos_individuos = []
		for _ in range(count):
			indv1, indv2 = sample(selecionados, 2)
			filho1, filho2 = self.umPonto(indv1, indv2)
			novos_individuos.extend((filho1, filho2))
		return novos_individuos

	def umPonto(self, indv1, indv2):
		ponto_corte = randint(0, Individuo().tamanho)
		filho1 = indv1.cromossomo[:ponto_corte] + indv2.cromossomo[ponto_corte:]
		filho2 = indv2.cromossomo[:ponto_corte] + indv1.cromossomo[ponto_corte:]
		return (Individuo(filho1), Individuo(filho2))

	def muta(self, populacao:list):
		for individuo in populacao:
			if random() < self.taxa_mutacao:
				self.permuta(individuo)

	def permuta(self, individuo:Individuo):
		i = 0
		for value in individuo.cromossomo:
			if random() >= 0.5:
				if value == 1:
					individuo.cromossomo[i] = 0
					return
				individuo.cromossomo[i] = 1
			i += 1

	def reproducao(self, populacao:list) -> list:
		populacao.sort(key=lambda individuo: individuo.fitness)
		count = int(self.tamanho_populacao * self.taxa_crossing_over)
		selecionados = self.seleciona(populacao)
		populacao_temp = self.cruza(selecionados)
		nova_populacao = populacao_temp + populacao[count:]
		self.muta(nova_populacao)
		return nova_populacao

	def produtos(self):  #Apresenta os itens da melhor solucao
		lista_produtos = self.geraProdutos()
		i = 0
		for value in self.melhor_individuo.cromossomo:
			if value == 1:
				print(lista_produtos[i])
			i += 1