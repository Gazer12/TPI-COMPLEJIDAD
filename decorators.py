import time

def delta_time(n):
    def count_elapsed_time(f):
        def w(*args, **kwargs):
            start_time = time.perf_counter()
            ret = f(*args, **kwargs)
            elapsed_time = (time.perf_counter()) - start_time
            
            # Ajuste de formato para la barra de progreso visual
            start = 20 - len(n)
            x = n
            for i in range(start):
                x += '-'
            
            print(x + "> Tiempo: %.4f Segundos." % elapsed_time)
            
            # Devuelve una tupla con el nombre, el tiempo y el resultado de la función
            return ((n, float('%.4f' % elapsed_time), ret))
        return w
    return count_elapsed_time
