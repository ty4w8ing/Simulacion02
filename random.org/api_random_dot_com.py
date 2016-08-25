from randomwrapy import *
import threading

def generar_random():
	return rrandom()

def worker(nombre):
	file = open(nombre, "w")
	for i in range(0,20000):
		numero = "%.50f" % generar_random()
		file.write(numero+'\n')
	file.close()

if __name__ == '__main__':
	threads = list()
	for i in range(50):
		ar = str(i)+".txt"
		t = threading.Thread(target=worker, args=(ar,))
		threads.append(t)
		t.start()
