from ambiente1 import Ambiente 


for _ in range(10):
	print(f'Teste: {_}')
	if __name__ == '__main__':
		ga = Ambiente()
		print(ga.start())
		ga.produtos()