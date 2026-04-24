from decorators import delta_time

@delta_time("GRUPO GN - MÁXIMA OPTIMIZACIÓN")

def amigos(tope):
    import array

    # 1. PRE-ASIGNACIÓN Y CACHÉ DE MÉTODOS
    # Usamos bytearray o array.array para sigma. 'I' es eficiente.
    sigma = array.array('I', [0] * (tope + 1))
    sp = array.array('I', [0] * (tope + 1))
    primos = [] # Las listas son ligeramente más rápidas que array.array para .append()
    
    # TRUCO DE VELOCIDAD: Localizar métodos y variables
    # Esto evita que Python busque en el diccionario global/clase en cada iteración.
    add_primo = primos.append
    sigma[1] = 1
    
    # 2. CRIBA LINEAL O(N) OPTIMIZADA
    for i in range(2, tope + 1):
        s_i = sigma[i]
        if s_i == 0:
            add_primo(i)
            s_i = i + 1
            sigma[i] = s_i
            sp[i] = s_i
        
        sp_i = sp[i] # Cache local del valor actual de sp
        
        for p in primos:
            proximo = i * p
            if proximo > tope:
                break
            
            if i % p == 0:
                # p ya es el menor factor primo de i
                new_sp = sp_i * p + 1
                sp[proximo] = new_sp
                sigma[proximo] = (s_i // sp_i) * new_sp
                break
            else:
                # p es un nuevo factor primo menor
                sp[proximo] = p + 1
                sigma[proximo] = s_i * (p + 1)

    # 3. EXTRACCIÓN DE PARES (Optimización con Memoryview y variables locales)
    resultado = []
    res_append = resultado.append
    view = memoryview(sigma)
    
    for i in range(2, tope):
        # s_i_prop: Suma de divisores propios
        s_i_prop = view[i] - i
        
        # Filtros encadenados (Python los evalúa de izquierda a derecha)
        if i < s_i_prop <= tope:
            if view[s_i_prop] - s_i_prop == i:
                res_append(i)
                res_append(s_i_prop)
                
    return resultado

if __name__ == "__main__":
    t = int(input("Ingrese tope: "))
    print(amigos(t))
