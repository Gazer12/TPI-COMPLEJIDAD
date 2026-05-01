#ESTE ES DE GEMINII EL MAS RAPIDO HASTA AHORA

from decorators import delta_time

@delta_time("GRUPO GN - MÁXIMA OPTIMIZACIÓN LINEAL")
def amigos(tope):  
    suma_divisores = [0] * (tope + 1)
    suma_potencias_menor_primo = [0] * (tope + 1)
    lista_primos = []
    
    agregar_primo = lista_primos.append
    suma_divisores[1] = 1
    
    # Fase 1: Criba Lineal (Euler) microoptimizada
    for i in range(2, tope + 1):
        # 1. Caché de variables locales para evitar múltiples lecturas en las listas
        s_div_i = suma_divisores[i]
        
        if not s_div_i:  # 2. 'not' evalúa ligeramente más rápido que '== 0'
            agregar_primo(i)
            p_mas_1 = i + 1
            s_div_i = p_mas_1
            suma_divisores[i] = p_mas_1
            suma_potencias_menor_primo[i] = p_mas_1
            
        spmp_i = suma_potencias_menor_primo[i]
        
        for primo in lista_primos:
            proximo = i * primo
            if proximo > tope:
                break
            
            # not (i % primo) es marginalmente más rápido que (i % primo == 0)
            if not i % primo: 
                nueva_suma_p = spmp_i * primo + 1
                suma_potencias_menor_primo[proximo] = nueva_suma_p
                suma_divisores[proximo] = (s_div_i // spmp_i) * nueva_suma_p
                break
            
            p_mas_1 = primo + 1
            suma_potencias_menor_primo[proximo] = p_mas_1
            suma_divisores[proximo] = s_div_i * p_mas_1

    # Fase 2: Búsqueda de amigos usando enumerate
    resultado = []
    agregar_resultado = resultado.append
    
    # 3. enumerate es más rápido que range(). Evitamos hacer un slice de la 
    # lista (como suma_divisores[2:]) para no clonar memoria en topes grandes.
    for i, s_div in enumerate(suma_divisores):
        if i < 2: 
            continue
            
        s_propia = s_div - i
        
        if i < s_propia <= tope:
            # 4. Evaluamos directamente contra la lista para omitir variables intermedias
            if suma_divisores[s_propia] - s_propia == i:
                agregar_resultado(i)
                agregar_resultado(s_propia)
                
    return resultado

if __name__ == "__main__":
    t = int(input("Ingrese tope: "))
    print(amigos(t))