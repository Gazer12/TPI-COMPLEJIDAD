from decorators import delta_time

@delta_time("GRUPO GN")
def amigos(tope):
    import array
    
    limite_extendido = int(tope * 1.3)
    limite_mitad = (limite_extendido // 2) + 1
    
    stop_criba = limite_extendido + 1 
    stop_busqueda = tope + 1
    
    sumas_multiplos = array.array('I', [1] * stop_criba)
    
    for i in range(2, limite_mitad):
        inicio_j = i * 2
        for j in range(inicio_j, stop_criba, i):
            sumas_multiplos[j] += i

    amigos = []
    add_amigo = amigos.append
    
    for i in range(2, stop_busqueda):
        posible_amigo = sumas_multiplos[i]
        
        if i < posible_amigo < stop_criba:
            if sumas_multiplos[posible_amigo] == i:
                add_amigo(i)
                add_amigo(posible_amigo)
                
    return amigos


if __name__ == "__main__":
    t = int(input("Ingrese tope: "))
    print(amigos(t))
