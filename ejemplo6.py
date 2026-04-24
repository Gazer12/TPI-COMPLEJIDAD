from decorators import delta_time

@delta_time("GRUPO GN")
def amigos(tope):
	sumas_multiplos = [1] * int(tope * 1.3)
	limite2 = len(sumas_multiplos)
	limite1 = limite2//2
	for i in range(2, limite1 + 1):			
		for j in range(i * 2, limite2, i):	
			sumas_multiplos[j] += i	
	amigos = []
	for i in range(2, tope):
		if sumas_multiplos[i] != 1:	
			posible_amigo = sumas_multiplos[i]	
			if i < posible_amigo < limite2:
				if sumas_multiplos[posible_amigo] ==  i:
					amigos.append(i)
					amigos.append(posible_amigo)
	return amigos

if __name__ == "__main__":
	tope = int(input("Ingrese tope: "))
	print(amigos(tope))