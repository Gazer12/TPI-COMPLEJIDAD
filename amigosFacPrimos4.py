from decorators import delta_time

@delta_time("GRUPO GN")
def amigos(tope):
    
    # Suma_divisores[n] guardara la funcion sigma(n)
    suma_divisores = [0] * (tope + 1)

    # Suma_potencias_menor_primo[n] guardara (1 + p + p^2 + ... + p^k)
    # Siendo p el menor factor primo de n y p^k la maxima potencia que lo divide
    suma_potencias_menor_primo = [0] * (tope + 1)

    lista_primos = []
    
    agregar_primo = lista_primos.append
    
    # Caso inicial para la criba
    suma_divisores[1] = 1

    # Cada numero se procesa una sola vez
    for i in range(2, tope + 1):
        if suma_divisores[i] == 0:
            # i es primo
            agregar_primo(i)
            # Para un primo p: sigma(p) = p + 1
            suma_divisores[i] = i + 1
            suma_potencias_menor_primo[i] = i + 1
        
        for primo in lista_primos:
            proximo = i * primo
            if proximo > tope:
                break
            
            if i % primo == 0:
                # El primo ya es el menor factor primo de i.
                nueva_suma_p = suma_potencias_menor_primo[i] * primo + 1
                suma_potencias_menor_primo[proximo] = nueva_suma_p

                # sigma(p^(k+1) * m) = sigma(m) * sigma(k+1) -> propiedad de sigma
                suma_divisores[proximo] = (suma_divisores[i] // suma_potencias_menor_primo[i]) * nueva_suma_p
                break
            else:
                # El primo es un nuevo factor menor (coprimo con i).
                suma_potencias_menor_primo[proximo] = primo + 1
                
                # De nuevo propiedad multiplicativa: sigma(p * i) = sigma(p) * sigma(i)
                suma_divisores[proximo] = suma_divisores[i] * (primo + 1)

    # Buscamos numeros amigos
    resultado = []
    agregar_resultado = resultado.append
    
    # Usamos un rango hasta tope + 1 para no ignorar el ultimo valor
    for i in range(2, tope + 1):
        # s_propia: Suma de los divisores menores que el numero mismo (sigma(i) - i)
        s_propia = suma_divisores[i] - i
        
        # Filtros: i < s_propia evita duplicados y perfectos y suma_divisores[s_propia] - s_propia == i verifica la amistad 
        if i < s_propia <= tope and suma_divisores[s_propia] - s_propia == i:
            agregar_resultado(i)
            agregar_resultado(s_propia)
                
    return resultado

if __name__ == "__main__":
    t = int(input("Ingrese tope: "))
    print(amigos(t))
