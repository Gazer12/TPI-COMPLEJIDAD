import time

def delta_time(n):
    def count_elapsed_time(f):
        def w(*args, **kwargs):
            start_time = time.perf_counter()
            ret = f(*args, **kwargs)
            elapsed_time = time.perf_counter() - start_time
            start = 20 - len(n)
            x = n
            for i in range(start):
                x += '-'
            print(x + "> Tiempo: %.4f Segundos." % elapsed_time)
            return ((n, float('%.4f' % elapsed_time), ret))
        return w
    return count_elapsed_time

def criba_sumas_optimizada(limite):
    # Volvemos a las listas nativas de Python (más rápidas para esto)
    sumas = [1] * (limite + 1)
    sumas[0] = sumas[1] = 0
    
    # Solo iteramos hasta la raíz cuadrada del límite
    raiz = int(limite ** 0.5)
    
    for i in range(2, raiz + 1):
        # El cuadrado de i suma solo i (no hay par distinto)
        sumas[i * i] += i
        
        # Iteramos desde el siguiente múltiplo
        for j in range(i * i + i, limite + 1, i):
            # Sumamos el divisor i, y su par (j // i) en un solo paso
            sumas[j] += i + j // i
            
    return sumas

@delta_time("Numeros Amigos")
def numeros_amigos(limite):
    sumas = criba_sumas_optimizada(limite)
    pares = []

    for a in range(2, limite + 1):
        b = sumas[a]
        if a < b <= limite and sumas[b] == a:
            pares.append((a, b))

    return pares

if __name__ == "__main__":
    limite = int(input("Ingresá el límite: "))
    _, tiempo, pares = numeros_amigos(limite)

    print(f"\nPares encontrados: {len(pares)}")
    for par in pares:
        print(f"  {par[0]} y {par[1]}")