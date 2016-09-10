import sys
import math
import collections


def printMatriz(matriz):
	s = [[str(e) for e in row] for row in matriz]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = "\t".join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print '\n'.join(table)

def cargar_archivo(filepath):
	lista = []
	with open( filepath, "r" ) as archivo:
		print "\t\tAnalisis del archivo:", archivo.name,"\n"
		for linea in archivo:
			lista.append( float( linea.rstrip() ) )
	archivo.close()	
	return lista
################################################################################################################################################################################################

def calcular_promedio(lista):
	return ( sum( lista ) / len( lista ) )
################################################################################################################################################################################################
def calcular_varianza(lista, promedio):
	ene_menos_uno = len(lista)
	varianza = 0
	for elemento in lista:
		varianza += (( elemento - promedio ) ** 2)
	return (varianza / ene_menos_uno) 

def calcular_desviacion_estandar(varianza):
	return math.sqrt(varianza)
################################################################################################################################################################################################


################################################################################################################################################################################################
def calcular_corridas_h(lista):
	h = 0
	signo = '*'
	for actual, siguiente in zip(lista, lista[1:]):
		temp = signo
		if actual <= siguiente:
			signo = '+'
		else:
			signo = '-'
		if temp != signo:
			h += 1
	return h

def calcular_corridas_esperanza(n):
	return float((2*n)-1)/3

def calcular_corridas_desviacion(n):
	return float( math.sqrt(((16*n)-29)/90) )

def calcular_corridas_z0(h, eh, sh):
	return float( (h-eh) / sh )

################################################################################################################################################################################################

def definir_tabla_poker(lista):
	diccionario = {"Diferentes": 0, "Par" : 0, "Dos Pares" : 0, "Tercia" : 0, "Full" : 0, "Poker" : 0, "Quintilla" : 0 }
	for elemento in lista:
		nuevo = str(elemento)[2:][:5]
		resultado = detectar_jugada(collections.Counter(nuevo))
		if resultado == 6:
			diccionario["Quintilla"] += 1
		elif resultado == 5:
			diccionario["Poker"] += 1
		elif resultado == 4:
			diccionario["Full"] += 1
		elif resultado == 3:
			diccionario["Tercia"] += 1
		elif resultado == 2:
			diccionario["Dos Pares"] += 1
		elif resultado == 1:
			diccionario["Par"] += 1
		elif resultado == 0:
			diccionario["Diferentes"] += 1
	return diccionario

def detectar_jugada(diccionario):
	lista = sorted(diccionario.values())
	maximo =  max(lista)
	if maximo == 5:
		return 6
	elif maximo == 4:
		return 5
	elif maximo == 3:
		lista.remove(3)
		if lista != []:
			maximo =  max(lista)
			if maximo == 2:
				return 4
			return 3
		else:
			return 3
	if maximo == 2:
		temp = 0
		for i in lista:
			if i == 2:
				temp += 1
		if temp == 2:
			return 2
		else:
			return 1
	else:
		return 0

def generar_matriz_poker(diccionario, largo):
	matriz = [ [ 0 for i in range(7) ] for j in range(8) ]
	matriz[0][0] = "Clase"
	matriz[1][0] = "Diferentes"
	matriz[2][0] = "Par"
	matriz[3][0] = "Dos Pares"
	matriz[4][0] = "Tercia"	
	matriz[5][0] = "Full"
	matriz[6][0] = "Poker"
	matriz[7][0] = "Quintilla"
	matriz[1][1] = diccionario["Diferentes"]
	matriz[2][1] = diccionario["Par"]
	matriz[3][1] = diccionario["Dos Pares"]
	matriz[4][1] = diccionario["Tercia"]
	matriz[5][1] = diccionario["Full"]
	matriz[6][1] = diccionario["Poker"]
	matriz[7][1] = diccionario["Quintilla"]
	matriz[0][1] = "fo"
	matriz[0][2] = "pe"
	matriz[0][3] = "fe"
	matriz[0][4] = "(fo-fe)    "
	matriz[0][5] = "**(fo-fe)^2"
	matriz[0][6] = "** / fe"
	matriz[1][2] = 0.30240
	matriz[2][2] = 0.50400
	matriz[3][2] = 0.10800
	matriz[4][2] = 0.07200
	matriz[5][2] = 0.00900
	matriz[6][2] = 0.00450
	matriz[7][2] = 0.00010

	for i in range(1,8):
		for j in range(3,8):
			if j == 3:
				matriz[i][j] = matriz[i][j-1]*largo
			if j == 4:
				matriz[i][j] = matriz[i][j-3]-matriz[i][j-1]
			if j == 5:
				matriz[i][j] = float("{:.4f}".format(float(matriz[i][j-1] ** 2)))
			if j == 6:
				matriz[i][j] = matriz[i][j-1] / matriz[i][j-3]
	return matriz

def calcular_x2_0_poker(matriz):
	x2_0 = 0
	for i in range(1,7):
		x2_0 += matriz[i][6]
	return x2_0


################################################################################################################################################################################################

def calcular_dicionario_series(lista):
	diccionario =  dict( zip(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
	for i, j in zip(lista, lista[1:]):
		temp = int(str(i)[2:][:1]) // 2
		temp2 = (int(str(j)[2:][:1]) // 2) * 5
		diccionario[str(temp+temp2+1)] += 1
	return diccionario

def calcular_matriz_series(diccionario, largo):
	matriz = [ [ 0 for i in range(6) ] for j in range(26) ]
	matriz[0][0] = "Celda"
	matriz[0][1] = "fo"
	matriz[0][2] = "fe"
	matriz[0][3] = "(fo-fe)    "
	matriz[0][4] = "**(fo-fe)^2"
	matriz[0][5] = "** / fe"
	c_cuadrado = float(largo - 1)/25
	for i in range(1,26):
		for j in range (6):
			if j == 0:
				matriz[i][0] = i
			elif j == 1:
				matriz[i][1] = diccionario.get(str(i))
			elif j == 2:
				matriz[i][2] = c_cuadrado
			elif j == 3:
				matriz[i][3] = matriz[i][1] - matriz[i][2]
			elif j == 4:
				matriz[i][4] = matriz[i][3] ** 2
			elif j == 5:
				matriz[i][5] = float("{:.4f}".format(float(matriz[i][4] / matriz[i][2])))
	return matriz			

def calcular_x2_0_series(matriz):
	sumando = 0
	for i in range(1, 26):
		sumando += matriz[i][5]
	return sumando


################################################################################################################################################################################################
if __name__ == '__main__':
	if len(sys.argv) == 3:
		lista = cargar_archivo( str(sys.argv[1]) )
		largo = len(lista)
		print lista[0]
		promedio = calcular_promedio( lista )
		varianza = calcular_varianza( lista, promedio )
		desviacion = calcular_desviacion_estandar(varianza)
		print "\nCantidad de lineas leidas\n\t(n) =",largo
		print "\nEl promedio es\n\tprom(x) =", promedio
		print "\nLa varianza es\n\tvar(x) = ", varianza
		print "\tDesviacion estandar = ", desviacion,"\n\n"
################################################################################################
		if str(sys.argv[2]) == "corridas":
			print "Prueba de Corridas"
			corridas_h = calcular_corridas_h(lista)
			corridas_esperanza = calcular_corridas_esperanza(largo)
			corridas_desviacion = calcular_corridas_desviacion(largo)
			corridas_zeta_subcero = calcular_corridas_z0(corridas_h, corridas_esperanza, corridas_desviacion)
			print "\th(x) = ", corridas_h
			print "\tE(h) = ", corridas_esperanza
			print "\ts(h) = ", corridas_desviacion
			print "\tz0 = ", corridas_zeta_subcero
################################################################################################
		elif str(sys.argv[2]) == "poker":
			print "Prueba de Poker"
			diccionario_poker = definir_tabla_poker(lista)
			poker_martiz = generar_matriz_poker(diccionario_poker, largo)
			poker_x2 = calcular_x2_0_poker(poker_martiz)
			print "Jugadas totales:"
			for key, value in diccionario_poker.iteritems():
				print key, value
			print "\n"
			printMatriz(poker_martiz)
			print "x2_0 = ", poker_x2
################################################################################################
		elif str(sys.argv[2]) == "series":
			print "Prueba de Series"
			serie_diccionario = calcular_dicionario_series(lista)
			matriz_series = calcular_matriz_series(serie_diccionario, largo)
			x2_series = calcular_x2_0_series(matriz_series)
			printMatriz(matriz_series)
			print "x2 = ",x2_series


	else:
		print "comando invalido"