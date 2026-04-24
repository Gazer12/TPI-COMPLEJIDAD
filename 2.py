import time
from array import array

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

def criba_sumas(limite):
    # Inicializamos todo en 1 directamente (el 1 es divisor de todos)
    # los indices 0 y 1 quedan en 0 porque no los usamos
    sumas = array('l', [0, 0] + [1] * (limite - 1))

    # Arrancamos desde 2, nos ahorramos el loop de i=1 entero
    for i in range(2, limite // 2 + 1):
        for j in range(2 * i, limite + 1, i):
            sumas[j] += i

    return sumas

@delta_time("Numeros Amigos")
def numeros_amigos(limite):
    sumas = criba_sumas(limite)
    pares = []

    for a in range(2, limite + 1):
        b = sumas[a]
        # b > a evita duplicados, b != a evita perfectos, b <= limite evita out of bounds
        if a < b <= limite and sumas[b] == a:
            pares.append((a, b))

    return pares

limite = int(input("Ingresá el límite: "))
resultado = numeros_amigos(limite)

_, tiempo, pares = resultado
print(f"\nPares encontrados: {len(pares)}")
for par in pares:
    print(f"  {par[0]} y {par[1]}")