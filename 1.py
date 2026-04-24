import time
from array import array  # modulo estandar, no hay que instalar nada

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

# ---- Criba con array nativo ----
def criba_sumas(limite):
    # 'l' = unsigned long, más eficiente que lista Python normal
    sumas = array('l', [0] * (limite + 1))
    
    for i in range(1, limite // 2 + 1):
        for j in range(2 * i, limite + 1, i):  # todos los multiplos de i
            sumas[j] += i
    
    return sumas

# ---- Función principal decorada ----
@delta_time("Numeros Amigos")
def numeros_amigos(limite):
    sumas = criba_sumas(limite)
    pares = []

    for a in range(2, limite + 1):
        b = sumas[a]
        if b > a and b <= limite and sumas[b] == a:
            pares.append((a, b))

    return pares

# ---- Ejecución ----
limite = int(input("Ingresá el límite: "))
resultado = numeros_amigos(limite)

_, tiempo, pares = resultado
print(f"\nPares encontrados: {len(pares)}")
for par in pares:
    print(f"  {par[0]} y {par[1]}")