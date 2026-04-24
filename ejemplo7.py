from decorators import delta_time

@delta_time("GRUPO GN - MÁXIMA OPTIMIZACIÓN")
def amigos(tope):
    import array
    
    # --- CÁLCULOS PREVIOS (Para no repetir operaciones en los bucles) ---
    limite_extendido = int(tope * 1.3)
    limite_mitad = (limite_extendido // 2) + 1
    # Guardamos el valor final para evitar el "+1" dentro de los for
    stop_criba = limite_extendido + 1 
    stop_busqueda = tope + 1
    
    # Inicialización masiva (mucho más rápido que un bucle manual)
    sumas_multiplos = array.array('I', [1] * stop_criba)
    
    # --- BUCLE DE CRIBADO ---
    for i in range(2, limite_mitad):
        # Sacamos el cálculo de i * 2 fuera del bucle interno
        inicio_j = i * 2
        for j in range(inicio_j, stop_criba, i):
            sumas_multiplos[j] += i

    amigos = []
    # Cache del método append para ganar microsegundos
    add_amigo = amigos.append
    
    # --- BUCLE DE EXTRACCIÓN ---
    for i in range(2, stop_busqueda):
        posible_amigo = sumas_multiplos[i]
        
        # Filtros rápidos: usamos las variables locales ya calculadas
        if i < posible_amigo < stop_criba:
            if sumas_multiplos[posible_amigo] == i:
                add_amigo(i)
                add_amigo(posible_amigo)
                
    return amigos

"""
from decorators import delta_time

@delta_time("GRUPO GN - MÁXIMA OPTIMIZACIÓN")
def amigos2(tope):
    import array
    
    # --- PRE-CÁLCULOS ---
    # Usar 1.2 es un poco más óptimo que 1.3 y sigue siendo muy seguro
    limite_extendido = int(tope * 1.2)
    stop_criba = limite_extendido + 1 
    limite_mitad = (limite_extendido >> 1) + 1 # bitwise shift para dividir por 2
    stop_busqueda = tope + 1
    
    # Inicialización masiva de memoria contigua
    sumas_multiplos = array.array('I', [1]) * stop_criba
    
    # --- NÚCLEO DEL ALGORITMO ---
    for i in range(2, limite_mitad):
        # Desplazamiento de bits para multiplicar por 2
        inicio_j = i << 1 
        for j in range(inicio_j, stop_criba, i):
            sumas_multiplos[j] += i
            
    amigos_lista = []
    add_amigo = amigos_lista.append
    
    # --- EXTRACCIÓN ---
    for i in range(2, stop_busqueda):
        pos_amigo = sumas_multiplos[i]
        
        # Filtro de comparación encadenada (Python lo hace muy rápido)
        if i < pos_amigo < stop_criba:
            if sumas_multiplos[pos_amigo] == i:
                add_amigo(i)
                add_amigo(pos_amigo)
                
    return amigos_lista
"""

if __name__ == "__main__":
    t = int(input("Ingrese tope: "))
    print(amigos(t))
