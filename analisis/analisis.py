import sys
import math

def cargar_archivo(filepath):
	lista = []
	with open( filepath, "r" ) as archivo:
		print "\t\tAnalisis del archivo:", archivo.name,"\n"
		for linea in archivo:
			lista.append( float( linea.rstrip() ) )
	archivo.close()	
	return lista


def calcular_promedio(lista):
	return ( sum( lista ) / len( lista ) )

def calcular_varianza(lista, promedio):
	ene_menos_uno = len(lista)
	varianza = 0
	for elemento in lista:
		varianza += (( elemento - promedio ) ** 2)
	return (varianza / ene_menos_uno) 

def calcular_desviacion_estandar(varianza):
	return math.sqrt(varianza)

################################################################################################
if __name__ == '__main__':
	if len(sys.argv) == 2:
		lista = cargar_archivo( str(sys.argv[1]) )
		promedio = calcular_promedio( lista )
		varianza = calcular_varianza( lista, promedio )
		desviacion = calcular_desviacion_estandar(varianza)

		print "\nCantidad de lineas leidas\n\t(n) =",len(lista)
		print "\nEl promedio es\n\tprom(x) =", promedio
		print "\nLa varianza es\n\tvar(x) = ", varianza
		print "\nLa deviacion estandar es\n\tdes_estandar(x) = ", desviacion
	else:
		print "comando invalido"