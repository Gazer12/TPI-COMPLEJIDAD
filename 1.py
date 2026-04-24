import time
import math

# ---- Decorator del profe ----
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

# ---- Suma de divisores propios en O(√n) ----
def suma_divisores(n):
    if n < 2:
        return 0
    total = 1
    sqrt_n = int(math.isqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

# ---- Función principal decorada ----
@delta_time("Numeros Amigos")
def numeros_amigos(limite):
    pares = []
    sumas = [suma_divisores(i) for i in range(limite + 1)]  # precalculo todo junto
    
    for a in range(2, limite + 1):
        b = sumas[a]
        # Condiciones: b es distinto de a, está en rango, y sumas[b] == a
        if b != a and b > a and b <= limite and sumas[b] == a:
            pares.append((a, b))
    
    return pares

# ---- Ejecución ----
limite = int(input("Ingresá el límite: "))
resultado = numeros_amigos(limite)

_, tiempo, pares = resultado
print(f"\nPares encontrados: {len(pares)}")
for par in pares:
    print(f"  {par[0]} y {par[1]}")