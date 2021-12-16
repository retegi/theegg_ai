import time


def suma_lineal(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

def suma_constante(n):
    return (n / 2) * (n +1)

cantidad = 1000000000

for i in range(4):
    t0 = time.time()
    suma1 = suma_lineal(cantidad)
    t1 = time.time()
    suma2 = suma_constante(cantidad)
    t2 = time.time()

print("{}   -   {}".format(suma1, t1-t0))
print("{}   -   {}".format(suma2, t2-t1))

cantidad *= 10