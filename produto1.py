class Produto:
	def __init__(self, nome, espaco, valor):
		self.nome = nome
		self.espaco = espaco
		self.valor = valor

	def __repr__(self):
		return f'Nome: {self.nome}, RS: {self.valor}, {self.espaco} m³\n'
