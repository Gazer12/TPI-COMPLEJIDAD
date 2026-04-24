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

@delta_time("Numeros Amigos")
def numeros_amigos(limite):
    # --- int32 + init con 1 (el divisor 1 ya incluido) ---
    sumas = array('i', [0, 0] + [1] * (limite - 1))
    
    mitad = limite // 2
    _range = range  # cache local

    # --- Criba: i=2 separado, luego solo impares ---
    for j in _range(4, limite + 1, 2):
        sumas[j] += 2

    for i in _range(3, mitad + 1, 2):        # solo impares
        s = sumas                              # cache local del array
        for j in _range(i + i, limite + 1, i):
            s[j] += i

    # --- Pares faltantes (4, 6, 8...) como divisores ---
    for i in _range(4, mitad + 1, 2):
        s = sumas
        for j in _range(i + i, limite + 1, i):
            s[j] += i

    # --- Busqueda vectorizada con list comprehension ---
    pares = [(a, sumas[a]) for a in _range(2, limite + 1)
             if a < sumas[a] <= limite and sumas[sumas[a]] == a]

    return pares

limite = int(input("Ingresá el límite: "))
resultado = numeros_amigos(limite)

_, tiempo, pares = resultado
print(f"\nPares encontrados: {len(pares)}")
for par in pares:
    print(f"  {par[0]} y {par[1]}")