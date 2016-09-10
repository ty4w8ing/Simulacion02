import random


def generar_random():
	return random.random()

def escribir_en_archivo():
	file = open("python.txt", "w")
	for i in range(0,1000000):
		numero = "%.10f" % generar_random()
		file.write(numero+'\n')
	file.close()

if __name__ == '__main__':
	escribir_en_archivo()